#!/usr/bin/env python3
"""Genera los dos zips de cada release. Solo usa la librería estándar.

    profe-ingles.zip         Para claude.ai (Skills). La carpeta de la skill va en la raíz del zip.
    profe-ingles-plugin.zip  Para Claude Code y para enviar al directorio. El plugin va en la raíz del zip.

Los zips son reproducibles: mismo contenido, mismo orden y fechas fijas, así que
el mismo commit siempre produce los mismos bytes.

Uso:
    python3 scripts/build_zips.py            # escribe en dist/
    python3 scripts/build_zips.py --out DIR
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

NAME = "profe-ingles"
ROOT = Path(__file__).resolve().parent.parent
PLUGIN_DIR = Path("plugins") / NAME
FIXED_DATE = (2020, 1, 1, 0, 0, 0)


def files_under(base: Path) -> list[Path]:
    return sorted(p for p in base.rglob("*") if p.is_file())


def write_zip(target: Path, entries: list[tuple[Path, str]]) -> None:
    """Escribe `entries` (ruta en disco, ruta dentro del zip) con orden y fechas fijos."""
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for source, arcname in sorted(entries, key=lambda e: e[1]):
            info = zipfile.ZipInfo(arcname, date_time=FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, source.read_bytes())


def build_skill_zip(root: Path, out: Path) -> Path:
    skill_dir = root / PLUGIN_DIR / "skills" / NAME
    entries = [(p, f"{NAME}/{p.relative_to(skill_dir).as_posix()}") for p in files_under(skill_dir)]
    target = out / f"{NAME}.zip"
    write_zip(target, entries)
    return target


def build_plugin_zip(root: Path, out: Path) -> Path:
    plugin_dir = root / PLUGIN_DIR
    entries = [(p, p.relative_to(plugin_dir).as_posix()) for p in files_under(plugin_dir)]
    target = out / f"{NAME}-plugin.zip"
    write_zip(target, entries)
    return target


def verify(skill_zip: Path, plugin_zip: Path) -> list[str]:
    """Comprueba que cada zip tiene la estructura que espera su destino."""
    errors: list[str] = []
    with zipfile.ZipFile(skill_zip) as zf:
        names = set(zf.namelist())
        if f"{NAME}/SKILL.md" not in names:
            errors.append(f"{skill_zip.name}: falta {NAME}/SKILL.md en la raíz")
        bad = [n for n in names if not n.startswith(f"{NAME}/")]
        if bad:
            errors.append(f"{skill_zip.name}: entradas fuera de {NAME}/: {sorted(bad)}")
        if zf.testzip() is not None:
            errors.append(f"{skill_zip.name}: zip corrupto")
    with zipfile.ZipFile(plugin_zip) as zf:
        names = set(zf.namelist())
        for required in (".claude-plugin/plugin.json", f"skills/{NAME}/SKILL.md"):
            if required not in names:
                errors.append(f"{plugin_zip.name}: falta {required}")
        if zf.testzip() is not None:
            errors.append(f"{plugin_zip.name}: zip corrupto")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    args = parser.parse_args(argv)

    skill_zip = build_skill_zip(args.root.resolve(), args.out)
    plugin_zip = build_plugin_zip(args.root.resolve(), args.out)

    errors = verify(skill_zip, plugin_zip)
    if errors:
        for err in errors:
            print(f"✘ {err}")
        return 1
    for path in (skill_zip, plugin_zip):
        print(f"✔ {path}  ({path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
