# Checklist del mantenedor (tareas 👤 del plan)

Todo lo que el plan asigna al mantenedor y que **no se puede hacer desde archivos**: son acciones en tus cuentas y en la configuración de GitHub. Los días corresponden al plan de ejecución v1. Marca cada casilla al terminar.

## Día 1: nombre, repo y plataforma

- [ ] Verificar que **`profe-ingles`** esté libre en GitHub, en redes (TikTok, X, Instagram) y como dominio. Es irreversible: si está ocupado, elige otro **antes** de publicar y avisa para renombrar la skill, el plugin y los manifiestos.
- [ ] El repositorio ya existe (`juancastro1330/skill-ingles`). Comprobar que es **público** y tiene licencia MIT.
- [ ] Confirmar que la **rama por defecto es `main`** (Settings → Branches). Si el primer push fue a otra rama, cámbiala aquí o renombra la rama.
- [ ] Settings → Actions → General → Workflow permissions: activar **«Allow GitHub Actions to create and approve pull requests»**. Sin esto, release-please no puede abrir el Release PR.
- [ ] En tu cuenta de Claude: mirar en Configuración si tu plan muestra **Skills** y activar la ejecución de código. Anotar el resultado en [`compatibilidad.md`](compatibilidad.md). Así sabrás qué capa puedes probar.
- [ ] Abrir un PR de prueba con un error (por ejemplo, un `name` con «claude») y comprobar que el CI **falla**, y que uno correcto **pasa**.

## Día 2: probar las instrucciones

- [ ] Pegar [`instrucciones/instrucciones-claude.md`](../instrucciones/instrucciones-claude.md) (el bloque de texto) en «Instrucciones para Claude».
- [ ] Confirmar que **cabe** en el campo. El validador limita el bloque a 2.000 caracteres como tope prudente, pero no es un dato oficial. Si el campo admite menos, acorta el texto.
- [ ] Usar Claude con normalidad y comprobar que el bloque aparece.

## Día 4: instalar la skill

- [ ] Generar los zips: `python3 scripts/build_zips.py` (o bajarlos del primer Release).
- [ ] Subir `dist/profe-ingles.zip` en claude.ai (Skills). Comprobar que aparece y se activa en un chat.
- [ ] Si usas Claude Code: `/plugin marketplace add juancastro1330/skill-ingles` y `/plugin install profe-ingles@profe-ingles`.

## Días 5 a 7: usarlo a diario

- [ ] Anotar cada fricción (qué molestó, qué sobró, qué faltó). Mínimo 10 notas.
- [ ] **Hito de la semana 1:** mantenerlo activo 5 días seguidos sin desactivarlo. Si no pasa, ajusta antes de mostrarlo a nadie.

| Fecha | Qué molestó / sobró / faltó | Gravedad (1-3) | Cambio propuesto |
|---|---|---|---|
| | | | |

## Semana 2: beta

- [ ] **Día 8:** reclutar de 5 a 10 hispanohablantes: varios niveles, planes Free y Pro, al menos la mitad no programadores. Mínimo 5 confirmados. Mensajes listos en [`beta/mensaje-reclutamiento.md`](beta/mensaje-reclutamiento.md).
- [ ] Usar el [kit de beta](beta/guia-beta.md). Comprobar que alguien lo instala sin ayuda.
- [ ] **Día 3 de la beta:** hacer el check-in («¿lo sigues usando? ¿qué te molesta?»).
- [ ] Correr los [evals de activación](../evals/activation.md) y los [ejemplos de referencia](../evals/golden-examples.md) en web, escritorio, móvil y Claude Code. Rellenar [`compatibilidad.md`](compatibilidad.md).
- [ ] **Día 14:** encuesta final y cálculo de retención (ver [`beta/formulario-beta.md`](beta/formulario-beta.md)).
- [ ] **Decisión:** si la retención es de al menos 60 % y hay cero errores graves en los evals, se lanza. Si no, una semana más de ajustes y una segunda ronda.

## Semana 3: publicar

**Día 15**

- [ ] Settings → Branches → regla para `main`:
  - Require a pull request before merging, con aprobación obligatoria.
  - Require review from Code Owners.
  - Require status checks: `Validar skill, manifiestos y evals`, `Título del PR en formato convencional` y `Buscar secretos (gitleaks)`.
  - Do not allow bypassing the above settings (o permite el bypass solo a administradores; ver la nota de abajo).
- [ ] Settings → General → Pull Requests: permitir solo **squash merge**, con el **título del PR** como mensaje del commit.
- [ ] Settings → Code security: activar **Dependabot alerts** y **security updates**, y **Private vulnerability reporting** (lo usa [`SECURITY.md`](../SECURITY.md)).
- [ ] Revisar `.github/CODEOWNERS`.
- [ ] Crear el token para release-please (ver la nota de abajo).

**Día 17**

- [ ] Grabar el video de instalación de 60 s (guion en [`beta/guion-video-60s.md`](beta/guion-video-60s.md)) y el GIF de antes y después. Guardar el GIF como `docs/demo.gif` y ponerlo en el README (hay un comentario que marca el lugar).
- [ ] Settings → General → Social preview: subir `docs/social-preview.png`.
- [ ] Settings → General → Topics: `claude-skills`, `agent-skills`, `claude-code-plugin`, `english-learning`, `esl`, `spanish-speakers`, `cefr`, `language-learning`.
- [ ] Activar **Discussions**.
- [x] Crear los 10 «good first issues» a partir de [`good-first-issues.md`](good-first-issues.md), con la etiqueta `good first issue`. Ya están creados (#1 a #10).

**Día 18**

- [ ] Para publicar la versión 1.0.0, incluye `Release-As: 1.0.0` al final del mensaje de un commit que llegue a `main` (release-please lo respeta). Después fusiona el **Release PR**.
- [ ] Comprobar que el Release trae `profe-ingles.zip` y `profe-ingles-plugin.zip`, y que el enlace directo del README funciona.
- [ ] Enviar el plugin al directorio de Anthropic siguiendo la guía oficial vigente.

**Días 19 a 21: lanzamiento escalonado** (mensajes por canal en [`lanzamiento/mensajes.md`](lanzamiento/mensajes.md))

- [ ] 1. Beta testers («Ya salió, compártelo si te sirvió»).
- [ ] 2. Creadores de inglés y comunidades hispanas (video «Aprende inglés mientras usas Claude»).
- [ ] 3. r/ClaudeAI, r/EnglishLearning y r/languagelearning (demo y utilidad, sin spam).
- [ ] 4. PRs a las 3 listas awesome-claude-skills (una línea de descripción).
- [ ] 5. Show HN, X y LinkedIn (ángulo técnico: la arquitectura de dos capas).

## Notas

### Un solo mantenedor y CODEOWNERS

GitHub no deja que el autor de un PR lo apruebe. Si eres el único mantenedor y exiges «Require review from Code Owners», no podrás fusionar tus propios PR. Tienes tres salidas:

1. Permitir el bypass a administradores en la regla de `main` (lo más simple para uno solo).
2. Añadir a un segundo revisor de confianza.
3. Dejar de exigir la revisión de code owners y conservar solo los status checks.

### El Release PR no lanza el CI

Los PR creados con el `GITHUB_TOKEN` por defecto **no disparan** otros workflows. Si `main` exige el CI, el Release PR se quedará esperando. Solución:

1. Crea un token de acceso personal *fine-grained* limitado a este repositorio, con permisos de **Contents** y **Pull requests** en lectura y escritura.
2. Guárdalo en Settings → Secrets and variables → Actions con el nombre **`RELEASE_PLEASE_TOKEN`**.

`release.yml` ya lo usa si existe y, si no, vuelve al `GITHUB_TOKEN`.

### Rollback (menos de 10 minutos)

- **Usuario:** descarga el zip del Release anterior y súbelo de nuevo.
- **Repositorio:** `git revert` del commit problemático en un PR `fix:`; el parche sale solo.
