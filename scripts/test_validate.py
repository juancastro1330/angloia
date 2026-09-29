#!/usr/bin/env python3
"""Pruebas de scripts/validate.py y scripts/build_zips.py (solo librería estándar).

Criterio del día 1 del plan: «un PR con error falla y uno correcto pasa».
Cada prueba copia el repo, lo rompe de una forma concreta y comprueba que
falla exactamente la comprobación esperada.

    python3 -m unittest discover -s scripts -p "test_*.py" -v
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_zips  # noqa: E402
import validate  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SKILL = validate.SKILL_REL
SKILL_MD = SKILL / "SKILL.md"


class RepoCase(unittest.TestCase):
    """Trabaja sobre una copia temporal del repo."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "repo"
        shutil.copytree(
            REPO,
            self.root,
            ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", "*.pyc"),
        )

    def tearDown(self) -> None:
        self._tmp.cleanup()

    # Ayudas -----------------------------------------------------------------
    def edit(self, rel: Path | str, fn) -> None:
        """Modifica un archivo de la copia. Falla si la modificación no cambia nada:
        una prueba que no rompe nada no prueba nada."""
        path = self.root / rel
        before = path.read_text(encoding="utf-8")
        after = fn(before)
        self.assertNotEqual(after, before, f"La modificación no cambió {rel}: la prueba no comprueba nada")
        path.write_text(after, encoding="utf-8")

    def current_version(self) -> str:
        """Versión actual del plugin. Cambia con cada release, así que no se escribe a mano."""
        path = self.root / validate.PLUGIN_REL / ".claude-plugin" / "plugin.json"
        return json.loads(path.read_text(encoding="utf-8"))["version"]

    def failing(self) -> dict[str, list[str]]:
        return {name: errs for name, errs in validate.run(self.root).items() if errs}

    def assertFailsOnly(self, check: str, needle: str) -> None:
        failed = self.failing()
        self.assertIn(check, failed, f"Debía fallar '{check}', fallaron: {list(failed)}")
        self.assertTrue(
            any(needle in e for e in failed[check]),
            f"Ningún error de '{check}' contiene «{needle}»: {failed[check]}",
        )


class TestValidRepo(RepoCase):
    def test_repo_correcto_pasa(self) -> None:
        self.assertEqual(self.failing(), {})

    def test_cli_devuelve_cero(self) -> None:
        self.assertEqual(validate.main(["--root", str(self.root)]), 0)


class TestSkillFormat(RepoCase):
    def test_nombre_con_claude(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("name: angloia", "name: angloia-claude", 1))
        self.assertFailsOnly("formato de SKILL.md", "claude")

    def test_nombre_no_coincide_con_la_carpeta(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("name: angloia", "name: otro-nombre", 1))
        self.assertFailsOnly("formato de SKILL.md", "debe coincidir con la carpeta")

    def test_nombre_con_mayusculas(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("name: angloia", "name: Anglo_IA", 1))
        self.assertFailsOnly("formato de SKILL.md", "minúsculas")

    def test_nombre_demasiado_largo(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("name: angloia", "name: " + "a" * 65, 1))
        self.assertFailsOnly("formato de SKILL.md", "máximo 64")

    def test_descripcion_demasiado_larga(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("---\n\n# AngloIA", "  " + "palabra " * 40 + "\n---\n\n# AngloIA", 1))
        self.assertFailsOnly("formato de SKILL.md", "máximo 1024")

    def test_descripcion_con_etiqueta_xml(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("Turns any", "Turns <b>any", 1))
        self.assertFailsOnly("formato de SKILL.md", "etiquetas XML")

    def test_descripcion_solo_en_ingles(self) -> None:
        self.edit(
            SKILL_MD,
            lambda t: re.sub(r"(?s)(description: >-\n).*?(\n---\n)", r"\1  Use it whenever the user asks.\2", t, count=1),
        )
        self.assertFailsOnly("formato de SKILL.md", "en español")

    def test_descripcion_con_dos_puntos_sin_comillas(self) -> None:
        self.edit(SKILL_MD, lambda t: re.sub(r"(?s)description: >-\n.*?(\n---\n)", r"description: Uso: tutor\1", t, count=1))
        self.assertFailsOnly("formato de SKILL.md", "': '")

    def test_cuerpo_de_500_lineas(self) -> None:
        self.edit(SKILL_MD, lambda t: t + "\nlínea\n" * 320)
        self.assertFailsOnly("formato de SKILL.md", "máximo 499")

    def test_sin_frontmatter(self) -> None:
        self.edit(SKILL_MD, lambda t: t.split("---\n", 2)[2])
        self.assertFailsOnly("formato de SKILL.md", "frontmatter")

    def test_clave_desconocida(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("name: angloia\n", "name: angloia\nfoo: bar\n", 1))
        self.assertFailsOnly("formato de SKILL.md", "claves no permitidas")


class TestSkillContents(RepoCase):
    def test_referencia_inexistente(self) -> None:
        (self.root / SKILL / "references" / "tenses.md").unlink()
        self.assertFailsOnly("contenido de la skill", "tenses.md")

    def test_enlace_a_referencia_rota(self) -> None:
        self.edit(SKILL_MD, lambda t: t + "\nVer `references/no-existe.md`.\n")
        self.assertFailsOnly("contenido de la skill", "no-existe.md")

    def test_referencia_huerfana(self) -> None:
        (self.root / SKILL / "references" / "extra.md").write_text("# Extra\n", encoding="utf-8")
        self.assertFailsOnly("contenido de la skill", "no está enlazada")

    def test_script_dentro_de_la_skill(self) -> None:
        (self.root / SKILL / "helper.py").write_text("print('hola')\n", encoding="utf-8")
        self.assertFailsOnly("contenido de la skill", "sin scripts")

    def test_url_dentro_de_la_skill(self) -> None:
        self.edit(SKILL_MD, lambda t: t + "\nMás en https://example.com\n")
        self.assertFailsOnly("contenido de la skill", "URL")

    def test_referencias_anidadas(self) -> None:
        self.edit(
            SKILL / "references" / "tenses.md",
            lambda t: t + "\nVer [más](cefr-levels.md).\n",
        )
        self.assertFailsOnly("contenido de la skill", "un solo nivel")

    def test_subcarpeta_en_references(self) -> None:
        sub = self.root / SKILL / "references" / "deep"
        sub.mkdir()
        (sub / "x.md").write_text("# x\n", encoding="utf-8")
        self.assertFailsOnly("contenido de la skill", "Carpeta no permitida")


class TestManifests(RepoCase):
    def test_versiones_distintas(self) -> None:
        self.edit(
            validate.PLUGIN_REL / ".claude-plugin" / "plugin.json",
            lambda t: t.replace(f'"version": "{self.current_version()}"', '"version": "99.0.0"'),
        )
        self.assertFailsOnly("manifiestos y versiones", "versiones distintas")

    def test_json_invalido(self) -> None:
        self.edit(".claude-plugin/marketplace.json", lambda t: t + "{")
        self.assertFailsOnly("manifiestos y versiones", "JSON válido")

    def test_source_inexistente(self) -> None:
        self.edit(
            ".claude-plugin/marketplace.json",
            lambda t: t.replace("./plugins/angloia", "./plugins/otro"),
        )
        self.assertFailsOnly("manifiestos y versiones", "source")

    def test_version_no_semver(self) -> None:
        version = self.current_version()
        for rel in (validate.PLUGIN_REL / ".claude-plugin" / "plugin.json", ".claude-plugin/marketplace.json", ".release-please-manifest.json"):
            self.edit(rel, lambda t: t.replace(version, "uno"))
        self.assertFailsOnly("manifiestos y versiones", "semver")


class TestInstructions(RepoCase):
    def test_texto_demasiado_largo(self) -> None:
        self.edit(validate.INSTRUCTIONS_REL, lambda t: t.replace("Además de asistente", "x" * 500 + " Además de asistente", 1))
        self.assertFailsOnly("instrucciones (capa 1)", "máximo 2000")

    def test_falta_un_comando(self) -> None:
        self.edit(validate.INSTRUCTIONS_REL, lambda t: t.replace("pausa inglés", "pausa"))
        self.assertFailsOnly("instrucciones (capa 1)", "pausa inglés")

    def test_skill_sin_un_comando(self) -> None:
        self.edit(SKILL_MD, lambda t: t.replace("inglés solo si pido", "otro"))
        self.assertFailsOnly("instrucciones (capa 1)", "SKILL.md no menciona")


class TestEvalsAndDocs(RepoCase):
    def test_faltan_ejemplos_dorados(self) -> None:
        self.edit("evals/golden-examples.md", lambda t: t.replace("## G30 ", "### G30 "))
        self.assertFailsOnly("evals", "ejemplos")

    def test_faltan_casos_de_activacion(self) -> None:
        self.edit("evals/activation.md", lambda t: t.replace("- **A20**", "- A20"))
        self.assertFailsOnly("evals", "que activan")

    def test_faltan_casos_que_no_activan(self) -> None:
        self.edit("evals/activation.md", lambda t: t.replace("- **N10**", "- N10"))
        self.assertFailsOnly("evals", "que no activan")

    def test_enlace_roto(self) -> None:
        self.edit("CONTRIBUTING.md", lambda t: t + "\n[roto](docs/no-existe.md)\n")
        self.assertFailsOnly("enlaces de los .md", "no-existe.md")

    def test_enlace_en_bloque_de_codigo_se_ignora(self) -> None:
        self.edit("CONTRIBUTING.md", lambda t: t + "\n```\n[ejemplo](docs/no-existe.md)\n```\n")
        self.assertNotIn("enlaces de los .md", self.failing())

    def test_readme_sin_aviso_de_no_afiliacion(self) -> None:
        self.edit("README.md", lambda t: re.sub(r"(?i)no está afiliado", "está cerca de", t))
        self.assertFailsOnly("READMEs", "no está afiliado")

    def test_falta_archivo_requerido(self) -> None:
        (self.root / "SECURITY.md").unlink()
        self.assertFailsOnly("archivos requeridos", "SECURITY.md")


class TestWorkflows(RepoCase):
    def test_action_sin_fijar_por_sha(self) -> None:
        self.edit(
            ".github/workflows/ci.yml",
            lambda t: re.sub(r"actions/checkout@[0-9a-f]{40}", "actions/checkout@v4", t, count=1),
        )
        self.assertFailsOnly("workflows", "SHA")

    def test_sin_permisos_de_nivel_superior(self) -> None:
        self.edit(".github/workflows/ci.yml", lambda t: t.replace("permissions: {}\n", "", 1))
        self.assertFailsOnly("workflows", "permissions")

    def test_titulo_de_pr_interpolado_en_run(self) -> None:
        self.edit(
            ".github/workflows/ci.yml",
            lambda t: t + "      - run: echo ${{ github.event.pull_request.title }}\n",
        )
        self.assertFailsOnly("workflows", "env")

    def test_titulo_de_pr_por_env_es_correcto(self) -> None:
        self.assertNotIn("workflows", self.failing())


class TestBuildZips(RepoCase):
    def build(self, out: Path) -> tuple[Path, Path]:
        skill = build_zips.build_skill_zip(self.root, out)
        plugin = build_zips.build_plugin_zip(self.root, out)
        return skill, plugin

    def test_estructura_de_los_zips(self) -> None:
        out = Path(self._tmp.name) / "dist"
        skill, plugin = self.build(out)
        self.assertEqual(build_zips.verify(skill, plugin), [])
        with zipfile.ZipFile(skill) as zf:
            names = zf.namelist()
        self.assertIn("angloia/SKILL.md", names)
        self.assertTrue(all(n.startswith("angloia/") for n in names))
        self.assertEqual(len([n for n in names if "/references/" in n]), 4)
        with zipfile.ZipFile(plugin) as zf:
            manifest = json.loads(zf.read(".claude-plugin/plugin.json"))
        self.assertEqual(manifest["name"], "angloia")

    def test_zips_reproducibles(self) -> None:
        first = self.build(Path(self._tmp.name) / "a")
        second = self.build(Path(self._tmp.name) / "b")
        for one, two in zip(first, second):
            self.assertEqual(one.read_bytes(), two.read_bytes(), f"{one.name} no es reproducible")

    def test_verify_detecta_zip_mal_formado(self) -> None:
        out = Path(self._tmp.name) / "bad"
        out.mkdir()
        skill, plugin = out / "s.zip", out / "p.zip"
        with zipfile.ZipFile(skill, "w") as zf:
            zf.writestr("SKILL.md", "x")
        with zipfile.ZipFile(plugin, "w") as zf:
            zf.writestr("otra-cosa.txt", "x")
        errors = build_zips.verify(skill, plugin)
        self.assertTrue(any("angloia/SKILL.md" in e for e in errors))
        self.assertTrue(any("plugin.json" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
