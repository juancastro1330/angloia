# Checklist del mantenedor (tareas 👤 del plan)

Todo lo que el plan asigna al mantenedor y que **no se puede hacer desde archivos**: son acciones en tus cuentas y en la configuración de GitHub. Los días corresponden al plan de ejecución v1. Marca cada casilla al terminar.

## Día 1: nombre, repo y plataforma

- [ ] Verificar que **`angloia`** esté libre en redes (TikTok, X, Instagram) y como dominio. Es irreversible: si está ocupado, elige otro **antes** de publicar. Ya se comprobó que en GitHub no existen repos ni cuentas con ese nombre, y que `angloia.com`, `.ai`, `.app`, `.es`, `.io`, `.org` y `.net` no tienen registro DNS; eso sugiere que no están en uso, pero **confirma la disponibilidad en un registrador** antes de comprar. Ojo: «Anglo» es un prefijo muy usado por academias de inglés en México; revisa que no genere confusión con una de ellas.
- [x] El repositorio existe (`juancastro1330/angloia`), es **público** y tiene licencia MIT.
- [x] La **rama por defecto es `main`** (Settings → General → Default branch).
- [x] Settings → Actions → General → Workflow permissions: **«Allow GitHub Actions to create and approve pull requests»** activado. Comprobado: release-please ya abrió sus Release PR.
- [ ] En tu cuenta de Claude: mirar en Configuración si tu plan muestra **Skills** y activar la ejecución de código. Anotar el resultado en [`compatibilidad.md`](compatibilidad.md). Así sabrás qué capa puedes probar.
- [x] Comprobar que el CI **pasa** con un PR correcto (lo hicieron el #11 y el #13). El caso con error (por ejemplo, un `name` con «claude») se cubre con las pruebas de `scripts/test_validate.py`; si quieres verlo también en GitHub, abre un PR de prueba con ese error.

## Día 2: probar las instrucciones

- [ ] Pegar [`instrucciones/instrucciones-claude.md`](../instrucciones/instrucciones-claude.md) (el bloque de texto) en «Instrucciones para Claude».
- [ ] Confirmar que **cabe** en el campo. El validador limita el bloque a 2.000 caracteres como tope prudente, pero no es un dato oficial. Si el campo admite menos, acorta el texto.
- [ ] Usar Claude con normalidad y comprobar que el bloque aparece.

## Día 4: instalar la skill

- [ ] Generar los zips: `python3 scripts/build_zips.py` (o bajarlos del primer Release).
- [ ] Subir `dist/angloia.zip` en claude.ai (Skills). Comprobar que aparece y se activa en un chat.
- [ ] Si usas Claude Code: `/plugin marketplace add juancastro1330/angloia` y `/plugin install angloia@angloia`.

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
- [ ] Settings → **Advanced Security**: activar **Dependabot alerts**, **Dependabot security updates** y **Private vulnerability reporting** (lo usa [`SECURITY.md`](../SECURITY.md)). Pasos en [«Paso a paso»](#paso-a-paso-para-los-ajustes-del-repositorio).
- [ ] Revisar `.github/CODEOWNERS`.
- [ ] Crear el token para release-please (ver la nota de abajo).

**Día 17**

- [ ] Grabar el video de instalación de 60 s (guion en [`beta/guion-video-60s.md`](beta/guion-video-60s.md)) y el GIF de antes y después. Guardar el GIF como `docs/demo.gif` y ponerlo en el README (hay un comentario que marca el lugar).
- [ ] Settings → General → Social preview: subir `docs/social-preview.png`.
- [ ] En la página principal del repo, a la derecha, **About** → ⚙: escribir la **descripción** y los **topics** `claude-skills`, `agent-skills`, `claude-code-plugin`, `english-learning`, `esl`, `spanish-speakers`, `cefr`, `language-learning`.
- [ ] Settings → General → Features: activar **Discussions**.
- [x] Crear los 10 «good first issues» a partir de [`good-first-issues.md`](good-first-issues.md), con la etiqueta `good first issue`. Ya están creados (#1 a #10).

**Día 18**

- [ ] Para publicar la versión 1.0.0, incluye `Release-As: 1.0.0` al final del mensaje de un commit que llegue a `main` (release-please lo respeta). Después fusiona el **Release PR**.
- [ ] Comprobar que el Release trae `angloia.zip` y `angloia-plugin.zip`, y que el enlace directo del README funciona.
- [ ] Enviar el plugin al directorio de Anthropic siguiendo la guía oficial vigente.

**Días 19 a 21: lanzamiento escalonado** (mensajes por canal en [`lanzamiento/mensajes.md`](lanzamiento/mensajes.md))

- [ ] 1. Beta testers («Ya salió, compártelo si te sirvió»).
- [ ] 2. Creadores de inglés y comunidades hispanas (video «Aprende inglés mientras usas Claude»).
- [ ] 3. r/ClaudeAI, r/EnglishLearning y r/languagelearning (demo y utilidad, sin spam).
- [ ] 4. PRs a las 3 listas awesome-claude-skills (una línea de descripción).
- [ ] 5. Show HN, X y LinkedIn (ángulo técnico: la arquitectura de dos capas).

## Paso a paso para los ajustes del repositorio

Estos ajustes solo se pueden hacer desde la web de GitHub, con tu sesión iniciada, en https://github.com/juancastro1330/angloia.

### Descripción y topics (2 minutos)

1. En la página principal del repositorio (pestaña **Code**), mira la columna de la derecha. Arriba está la caja **About**.
2. Pulsa el engranaje ⚙ que está a la derecha de la palabra **About**. Se abre una ventana llamada «Edit repository details».
3. En **Description**, pega este texto:

   > Tutor de inglés para hispanohablantes: escribes en español, Claude resuelve tu consulta y al final te enseña cómo decir tu mensaje en inglés. Skill y plugin de código abierto para Claude.

4. En **Topics**, haz clic en el cuadro, escribe un topic y pulsa **Enter**. Repite con cada uno: `claude-skills`, `agent-skills`, `claude-code-plugin`, `english-learning`, `esl`, `spanish-speakers`, `cefr`, `language-learning`. Los topics sirven para que la gente encuentre el repositorio al buscar en GitHub.
5. Deja **Website** vacío por ahora y pulsa **Save changes**.

### Private vulnerability reporting (1 minuto)

Permite que alguien que encuentre un problema de seguridad te lo cuente en privado, sin publicarlo. [`SECURITY.md`](../SECURITY.md) ya manda a la gente a ese botón, pero no aparece hasta que lo activas.

1. Ve a **Settings** (la última pestaña de la barra superior del repositorio).
2. En el menú de la izquierda, dentro de «Security and quality», pulsa **Advanced Security**.
3. Busca la línea **Private vulnerability reporting** y pulsa **Enable**.
4. En la misma página, pulsa **Enable** también en **Dependabot alerts** y en **Dependabot security updates**. Avisan si una dependencia tiene un problema de seguridad; aquí solo aplican a las actions de GitHub.

### Discussions (30 segundos)

1. **Settings** → **General**.
2. Baja hasta la sección **Features** y marca **Discussions**.

### Imagen social (1 minuto)

Es la imagen que sale cuando alguien comparte el enlace del repositorio.

1. Abre `docs/social-preview.png` en el repositorio, pulsa el botón de descarga (⬇ «Download raw file») y guárdala en tu computadora.
2. **Settings** → **General** → baja hasta **Social preview** → **Edit** → **Upload an image** y elige el archivo.

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
