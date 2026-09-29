#!/usr/bin/env python3
"""Valida el repositorio de Profe Inglés. Solo usa la librería estándar.

Cada comprobación devuelve una lista de errores (vacía si todo está bien).
Código de salida: 0 si no hay errores, 1 si hay alguno.

Uso:
    python3 scripts/validate.py            # valida el repo actual
    python3 scripts/validate.py --root DIR # valida otra copia
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Callable

SKILL_NAME = "profe-ingles"
SKILL_REL = Path("plugins") / SKILL_NAME / "skills" / SKILL_NAME
PLUGIN_REL = Path("plugins") / SKILL_NAME
INSTRUCTIONS_REL = Path("instrucciones") / "instrucciones-claude.md"

# Límites de la especificación de skills.
MAX_NAME_CHARS = 64
MAX_DESCRIPTION_CHARS = 1024
MAX_BODY_LINES = 499  # el cuerpo debe tener menos de 500 líneas
RESERVED_WORDS = ("claude", "anthropic")
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

# Tope prudente para el texto de la capa 1. No es un dato oficial: se confirma
# pegándolo en la cuenta real (día 2 del plan).
MAX_INSTRUCTIONS_CHARS = 2000

REQUIRED_REFERENCES = (
    "false-friends.md",
    "prepositions-and-word-order.md",
    "tenses.md",
    "cefr-levels.md",
)

# Comandos que deben estar tanto en las instrucciones como en la skill.
COMMANDS = (
    "modo ligero",
    "modo completo",
    "modo reto",
    "modo conversación",
    "pausa inglés",
    "sigue inglés",
    "inglés siempre",
    "inglés a veces",
    "inglés solo si pido",
    "mi nivel es",
    "resumen",
)

MIN_GOLDEN = 30
MIN_ACTIVATE = 20
MIN_NO_ACTIVATE = 10
MIN_EDGE_CASES = 10

REQUIRED_FILES = (
    "README.md",
    "README.en.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "release-please-config.json",
    ".release-please-manifest.json",
    "scripts/validate.py",
    "scripts/build_zips.py",
    ".github/workflows/ci.yml",
    ".github/workflows/release.yml",
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    "evals/golden-examples.md",
    "evals/activation.md",
    "evals/edge-cases.md",
)

SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
XML_TAG = re.compile(r"</?[A-Za-z][^>\n]*>")
URL = re.compile(r"https?://|www\.", re.IGNORECASE)
PINNED = re.compile(r"^[0-9a-f]{40}$")


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str], list[str]]:
    """Lee el frontmatter de un SKILL.md. Devuelve (datos, líneas del cuerpo, errores).

    Soporta el subconjunto de YAML que usan las skills: `clave: valor`, valores
    entre comillas y bloques `>` / `|`. Rechaza los escalares simples con `: ` o
    ` #`, que otros lectores de YAML interpretarían distinto.
    """
    errors: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines, ["SKILL.md debe empezar con una línea '---' (frontmatter)"]
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, lines, ["El frontmatter de SKILL.md no se cierra con '---'"]

    fm = lines[1:end]
    body = lines[end + 1:]
    data: dict[str, str] = {}
    i = 0
    while i < len(fm):
        line = fm[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line[0] in " \t":
            errors.append(f"Frontmatter: sangría inesperada en la línea {i + 2}: {line!r}")
            i += 1
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):(?:[ \t]+(.*))?$", line)
        if not m:
            errors.append(f"Frontmatter: línea no válida ({i + 2}): {line!r}")
            i += 1
            continue
        key, raw = m.group(1), (m.group(2) or "").strip()
        i += 1
        if key in data:
            errors.append(f"Frontmatter: la clave '{key}' está repetida")
        if re.fullmatch(r"[>|][+-]?", raw):
            block: list[str] = []
            while i < len(fm) and (not fm[i].strip() or fm[i][0] in " \t"):
                block.append(fm[i].strip())
                i += 1
            value = " ".join(b for b in block if b) if raw.startswith(">") else "\n".join(block)
            data[key] = value.strip()
        elif raw[:1] in ("'", '"'):
            if len(raw) < 2 or raw[-1] != raw[0]:
                errors.append(f"Frontmatter: '{key}' tiene comillas sin cerrar")
                data[key] = raw
            else:
                inner = raw[1:-1]
                data[key] = inner.replace("''", "'") if raw[0] == "'" else inner.replace('\\"', '"')
        else:
            if ": " in raw or " #" in raw:
                errors.append(
                    f"Frontmatter: '{key}' contiene ': ' o ' #' sin comillas; "
                    "usa comillas o un bloque '>-'"
                )
            data[key] = raw
    return data, body, errors


def strip_code_fences(text: str) -> str:
    """Quita los bloques de código delimitados por ``` para no analizar su contenido."""
    out: list[str] = []
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append(line)
    return "\n".join(out)


def first_code_block(text: str) -> str | None:
    m = re.search(r"^```[^\n]*\n(.*?)\n```", text, re.DOTALL | re.MULTILINE)
    return m.group(1) if m else None


def load_json(path: Path, errors: list[str]) -> dict | None:
    try:
        data = json.loads(read(path))
    except FileNotFoundError:
        errors.append(f"Falta {path.as_posix()}")
        return None
    except json.JSONDecodeError as exc:
        errors.append(f"{path.as_posix()} no es JSON válido: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{path.as_posix()} debe ser un objeto JSON")
        return None
    return data


# --------------------------------------------------------------------------
# Comprobaciones
# --------------------------------------------------------------------------

def check_required_files(root: Path) -> list[str]:
    errors = [f"Falta el archivo {rel}" for rel in REQUIRED_FILES if not (root / rel).is_file()]
    license_file = root / "LICENSE"
    if license_file.is_file() and "MIT License" not in read(license_file):
        errors.append("LICENSE debe ser la licencia MIT")
    return errors


def check_skill_format(root: Path) -> list[str]:
    errors: list[str] = []
    skill_dir = root / SKILL_REL
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"Falta {SKILL_REL.as_posix()}/SKILL.md"]

    data, body, fm_errors = parse_frontmatter(read(skill_md))
    errors.extend(fm_errors)

    unknown = sorted(set(data) - ALLOWED_FRONTMATTER_KEYS)
    if unknown:
        errors.append(f"Frontmatter: claves no permitidas: {', '.join(unknown)}")

    name = data.get("name", "")
    if not name:
        errors.append("Frontmatter: falta 'name'")
    else:
        if len(name) > MAX_NAME_CHARS:
            errors.append(f"'name' tiene {len(name)} caracteres (máximo {MAX_NAME_CHARS})")
        if not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append("'name' solo admite minúsculas, números y guiones")
        for word in RESERVED_WORDS:
            if word in name.lower():
                errors.append(f"'name' no puede contener la palabra '{word}'")
        if name != skill_dir.name:
            errors.append(f"'name' ({name}) debe coincidir con la carpeta ({skill_dir.name})")
        if name != SKILL_NAME:
            errors.append(f"'name' debe ser '{SKILL_NAME}' (nombre acordado del proyecto)")

    description = data.get("description", "")
    if not description:
        errors.append("Frontmatter: falta 'description' o está vacía")
    else:
        if len(description) > MAX_DESCRIPTION_CHARS:
            errors.append(
                f"'description' tiene {len(description)} caracteres (máximo {MAX_DESCRIPTION_CHARS})"
            )
        if XML_TAG.search(description):
            errors.append("'description' no puede contener etiquetas XML")
        low = description.lower()
        if not any(w in low for w in ("use it", "when ", "whenever")):
            errors.append("'description' debe explicar cuándo usarla en inglés (p. ej. 'Use it whenever…')")
        if not any(w in low for w in ("úsala", "cuando ")):
            errors.append("'description' debe explicar cuándo usarla en español (p. ej. 'Úsala cuando…')")

    if len(body) > MAX_BODY_LINES:
        errors.append(f"El cuerpo de SKILL.md tiene {len(body)} líneas (máximo {MAX_BODY_LINES})")
    return errors


def check_skill_contents(root: Path) -> list[str]:
    """La v1 no lleva scripts ni URLs; las referencias van a un solo nivel."""
    errors: list[str] = []
    skill_dir = root / SKILL_REL
    if not skill_dir.is_dir():
        return [f"Falta la carpeta {SKILL_REL.as_posix()}"]
    skill_md = skill_dir / "SKILL.md"
    refs_dir = skill_dir / "references"

    for path in sorted(skill_dir.rglob("*")):
        if path.is_dir():
            if path != refs_dir:
                errors.append(f"Carpeta no permitida dentro de la skill: {path.relative_to(root).as_posix()}")
            continue
        rel = path.relative_to(skill_dir)
        if rel.as_posix() != "SKILL.md" and not (rel.parent == Path("references") and path.suffix == ".md"):
            errors.append(
                f"Archivo no permitido en la skill v1: {rel.as_posix()} "
                "(solo SKILL.md y references/*.md; sin scripts)"
            )
            continue
        if URL.search(read(path)):
            errors.append(f"{rel.as_posix()} contiene una URL; la v1 no lleva URLs externas")

    for name in REQUIRED_REFERENCES:
        if not (refs_dir / name).is_file():
            errors.append(f"Falta la referencia references/{name}")

    if skill_md.is_file():
        text = read(skill_md)
        mentioned = set(re.findall(r"references/([\w.-]+\.md)", text))
        for name in sorted(mentioned):
            if not (refs_dir / name).is_file():
                errors.append(f"SKILL.md enlaza references/{name}, que no existe")
        if refs_dir.is_dir():
            for path in sorted(refs_dir.glob("*.md")):
                if path.name not in mentioned:
                    errors.append(f"references/{path.name} no está enlazada desde SKILL.md")
            for path in sorted(refs_dir.glob("*.md")):
                ref_text = strip_code_fences(read(path))
                if re.search(r"\]\([^)]*\.md[^)]*\)|references/", ref_text):
                    errors.append(
                        f"references/{path.name} enlaza a otro archivo; las referencias van a un solo nivel"
                    )
    return errors


def check_plugin_manifests(root: Path) -> list[str]:
    errors: list[str] = []
    plugin = load_json(root / PLUGIN_REL / ".claude-plugin" / "plugin.json", errors)
    market = load_json(root / ".claude-plugin" / "marketplace.json", errors)
    manifest = load_json(root / ".release-please-manifest.json", errors)
    config = load_json(root / "release-please-config.json", errors)

    plugin_version = None
    if plugin:
        if plugin.get("name") != SKILL_NAME:
            errors.append(f"plugin.json: 'name' debe ser '{SKILL_NAME}'")
        plugin_version = plugin.get("version")
        if not isinstance(plugin_version, str) or not SEMVER.match(plugin_version):
            errors.append(f"plugin.json: 'version' no es semver válido: {plugin_version!r}")
        if not plugin.get("description"):
            errors.append("plugin.json: falta 'description'")

    if market:
        for key in ("name", "owner", "plugins"):
            if key not in market:
                errors.append(f"marketplace.json: falta '{key}'")
        if not isinstance(market.get("owner"), dict) or not market.get("owner", {}).get("name"):
            errors.append("marketplace.json: 'owner.name' es obligatorio")
        for word in RESERVED_WORDS:
            if word in str(market.get("name", "")).lower():
                errors.append(f"marketplace.json: el nombre no puede contener '{word}'")
        entries = [p for p in market.get("plugins", []) if isinstance(p, dict) and p.get("name") == SKILL_NAME]
        if len(entries) != 1:
            errors.append(f"marketplace.json: debe haber exactamente un plugin '{SKILL_NAME}'")
        else:
            entry = entries[0]
            source = entry.get("source")
            if not isinstance(source, str) or not (root / source / ".claude-plugin" / "plugin.json").is_file():
                errors.append(f"marketplace.json: 'source' ({source!r}) no apunta a un plugin existente")
            if plugin_version and entry.get("version") != plugin_version:
                errors.append(
                    f"marketplace.json ({entry.get('version')}) y plugin.json ({plugin_version}) "
                    "tienen versiones distintas"
                )

    if manifest and plugin_version and manifest.get(".") != plugin_version:
        errors.append(
            f".release-please-manifest.json ({manifest.get('.')}) y plugin.json ({plugin_version}) "
            "tienen versiones distintas"
        )

    if config:
        pkg = config.get("packages", {}).get(".", {})
        for extra in pkg.get("extra-files", []):
            path = extra.get("path") if isinstance(extra, dict) else extra
            if not path or not (root / path).is_file():
                errors.append(f"release-please-config.json: extra-file inexistente: {path!r}")
    return errors


def check_instructions(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / INSTRUCTIONS_REL
    if not path.is_file():
        return [f"Falta {INSTRUCTIONS_REL.as_posix()}"]
    text = read(path)
    block = first_code_block(text)
    if block is None:
        return [f"{INSTRUCTIONS_REL.as_posix()} debe contener el texto para pegar en un bloque de código"]
    if len(block) > MAX_INSTRUCTIONS_CHARS:
        errors.append(
            f"El texto para pegar tiene {len(block)} caracteres (máximo {MAX_INSTRUCTIONS_CHARS})"
        )
    low = block.lower()
    for command in COMMANDS:
        if command not in low:
            errors.append(f"Las instrucciones no mencionan el comando '{command}'")

    skill_md = root / SKILL_REL / "SKILL.md"
    if skill_md.is_file():
        skill_low = read(skill_md).lower()
        for command in COMMANDS:
            if command not in skill_low:
                errors.append(f"SKILL.md no menciona el comando '{command}'")
    return errors


def count_items(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, re.MULTILINE))


def check_evals(root: Path) -> list[str]:
    errors: list[str] = []
    evals = root / "evals"

    golden = evals / "golden-examples.md"
    if golden.is_file():
        n = count_items(read(golden), r"^## G\d{2} ")
        if n < MIN_GOLDEN:
            errors.append(f"evals/golden-examples.md tiene {n} ejemplos (mínimo {MIN_GOLDEN})")

    activation = evals / "activation.md"
    if activation.is_file():
        text = read(activation)
        yes = count_items(text, r"^- \*\*A\d{2}\*\*")
        no = count_items(text, r"^- \*\*N\d{2}\*\*")
        if yes < MIN_ACTIVATE:
            errors.append(f"evals/activation.md tiene {yes} casos que activan (mínimo {MIN_ACTIVATE})")
        if no < MIN_NO_ACTIVATE:
            errors.append(f"evals/activation.md tiene {no} casos que no activan (mínimo {MIN_NO_ACTIVATE})")

    edge = evals / "edge-cases.md"
    if edge.is_file():
        n = count_items(read(edge), r"^## E\d{2} ")
        if n < MIN_EDGE_CASES:
            errors.append(f"evals/edge-cases.md tiene {n} casos (mínimo {MIN_EDGE_CASES})")
    return errors


def check_markdown_links(root: Path) -> list[str]:
    """Los enlaces relativos de los .md deben apuntar a archivos que existen."""
    errors: list[str] = []
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part in (".git", "dist", "node_modules") for part in rel.parts):
            continue
        for target in link.findall(strip_code_fences(read(path))):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            if not (path.parent / target).exists():
                errors.append(f"{rel.as_posix()}: enlace roto a '{target}'")
    return errors


def check_readmes(root: Path) -> list[str]:
    errors: list[str] = []
    checks = (
        ("README.md", ("no está afiliado", "instrucciones/instrucciones-claude.md", "/plugin marketplace add")),
        ("README.en.md", ("not affiliated", "instrucciones/instrucciones-claude.md", "/plugin marketplace add")),
    )
    for name, needles in checks:
        path = root / name
        if not path.is_file():
            continue
        low = read(path).lower()
        for needle in needles:
            if needle.lower() not in low:
                errors.append(f"{name} debe incluir «{needle}»")
    return errors


def check_workflows(root: Path) -> list[str]:
    """Permisos mínimos y actions fijadas por SHA."""
    errors: list[str] = []
    wf_dir = root / ".github" / "workflows"
    if not wf_dir.is_dir():
        return ["Falta la carpeta .github/workflows"]
    for path in sorted(wf_dir.glob("*.yml")):
        text = read(path)
        rel = path.relative_to(root).as_posix()
        if not re.search(r"^permissions:", text, re.MULTILINE):
            errors.append(f"{rel}: falta 'permissions:' de nivel superior (permisos mínimos)")
        for m in re.finditer(r"^\s*-?\s*uses:\s*(\S+)", text, re.MULTILINE):
            ref = m.group(1).strip("\"'")
            if ref.startswith("./"):
                continue
            action, _, version = ref.partition("@")
            if not PINNED.match(version):
                errors.append(f"{rel}: la action '{action}' debe fijarse por SHA de 40 caracteres, no por '{version}'")
        for lineno, line in enumerate(text.splitlines(), 1):
            untrusted = re.search(r"\$\{\{[^}]*github\.event\.(pull_request|issue)\.(title|body)", line)
            if untrusted and not re.match(r"^\s+[A-Z][A-Z0-9_]*:\s*\$\{\{", line):
                errors.append(
                    f"{rel}:{lineno}: no interpoles títulos o cuerpos de PR/issue directamente; "
                    "pásalos por una variable de 'env'"
                )
    return errors


CHECKS: dict[str, Callable[[Path], list[str]]] = {
    "archivos requeridos": check_required_files,
    "formato de SKILL.md": check_skill_format,
    "contenido de la skill": check_skill_contents,
    "manifiestos y versiones": check_plugin_manifests,
    "instrucciones (capa 1)": check_instructions,
    "evals": check_evals,
    "enlaces de los .md": check_markdown_links,
    "READMEs": check_readmes,
    "workflows": check_workflows,
}


def run(root: Path) -> dict[str, list[str]]:
    return {name: fn(root) for name, fn in CHECKS.items()}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)
    root = args.root.resolve()

    results = run(root)
    total = 0
    for name, errors in results.items():
        if errors:
            print(f"✘ {name}")
            for err in errors:
                print(f"    - {err}")
            total += len(errors)
        else:
            print(f"✔ {name}")

    if total:
        print(f"\n{total} error(es) de validación.")
        return 1
    print("\nTodo correcto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
