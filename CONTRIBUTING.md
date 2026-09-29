# Cómo contribuir

¡Gracias por querer ayudar! AngloIA es un proyecto comunitario para hispanohablantes que aprenden inglés. Cualquier mejora cuenta: un falso amigo nuevo, un ejemplo, una corrección de redacción.

## Principios

1. **Un cambio de texto en la skill equivale a un cambio de código.** Modifica lo que Claude hace en la cuenta de cada usuario, así que se revisa con el mismo cuidado (por eso `CODEOWNERS` cubre la skill, las referencias y las instrucciones).
2. **Ejemplos inventados, nunca conversaciones reales.** No pegues chats tuyos ni de nadie, ni datos personales, en issues, PR o ejemplos.
3. **Ante la duda, no corrijas.** Una corrección falsa hace más daño que una omisión.
4. **La tarea del usuario va primero.** El inglés va al final y es breve.

## Qué puedes aportar

- Falsos amigos nuevos en `plugins/angloia/skills/angloia/references/false-friends.md`, con su significado real y la forma correcta.
- Ejemplos nuevos en `evals/golden-examples.md`, casos de activación en `evals/activation.md` y casos límite en `evals/edge-cases.md`.
- Correcciones de traducción, ortografía o redacción.
- Mejoras del validador y de sus pruebas.

Hay ideas para empezar en [`docs/good-first-issues.md`](docs/good-first-issues.md).

## Antes de abrir un PR

1. Haz un fork y crea una rama.
2. Ejecuta las comprobaciones en local (solo necesitan Python 3):

   ```bash
   python3 scripts/validate.py
   python3 -m unittest discover -s scripts -p "test_*.py" -v
   ```

3. Si cambias el comportamiento de la skill, añade o ajusta un ejemplo en `evals/`.
4. Si cambias `description`, repite las 30 pruebas de `evals/activation.md`.

## Título del PR: formato convencional

El título del PR **debe** seguir [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/), porque los PR se fusionan con *squash* y ese título genera el versionado y el changelog automáticamente:

| Prefijo | Cuándo | Efecto en la versión |
|---|---|---|
| `feat:` | Una función o un comportamiento nuevo | menor (0.1.0 → 0.2.0) |
| `fix:` | Una corrección (traducción, falso amigo, bug) | parche (0.1.0 → 0.1.1) |
| `feat!:` | Un cambio que rompe algo (por ejemplo, un comando renombrado) | mayor |
| `docs:`, `chore:`, `ci:`, `test:`, `refactor:` | Todo lo demás | sin versión nueva |

Ejemplos: `feat: añade el modo entrevista`, `fix: corrige la explicación de "actually"`, `docs: aclara la instalación en móvil`.

## Reglas técnicas de la skill

`scripts/validate.py` las comprueba en cada PR:

- El `name` de la skill tiene como máximo 64 caracteres, solo minúsculas, números y guiones, no contiene «claude» ni «anthropic» y coincide con el nombre de la carpeta.
- La `description` tiene como máximo 1.024 caracteres, no lleva etiquetas XML y explica qué hace y cuándo usarla, en inglés y en español.
- El cuerpo de `SKILL.md` tiene menos de 500 líneas. El detalle va en `references/`, a un solo nivel de profundidad.
- La v1 **no lleva scripts ni URLs externas** dentro de la skill.
- Las actions de GitHub se fijan por SHA, con permisos mínimos por job.

## Reportar errores

- **Traducción o explicación incorrecta:** usa la plantilla «Error de traducción o explicación». Los errores graves (información falsa, un falso amigo mal explicado) tienen prioridad.
- **La skill no se activa, o se activa cuando no debe:** usa la plantilla de activación.
- **Vulnerabilidades:** no abras un issue público; sigue [`SECURITY.md`](SECURITY.md).

## Comportamiento esperado

Sé amable y paciente: muchas personas aquí están aprendiendo. Las críticas se dirigen al texto, no a las personas.
