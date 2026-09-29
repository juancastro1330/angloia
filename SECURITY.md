# Política de seguridad

## Versiones con soporte

Solo se corrige la última versión publicada (el Release más reciente).

## Cómo reportar una vulnerabilidad

**No abras un issue público.** Usa el reporte privado de GitHub:

1. Ve a la pestaña **Security** de este repositorio.
2. Pulsa **Report a vulnerability**.
3. Describe el problema y cómo reproducirlo.

*(To report a vulnerability privately, use the **Security** tab → **Report a vulnerability**. Please do not open a public issue.)*

Este es un proyecto comunitario: se responde lo antes posible, pero no hay un plazo garantizado.

## Qué cuenta como problema de seguridad

- Un cambio malicioso o sospechoso en `SKILL.md`, en las referencias o en las instrucciones, por ejemplo una orden escondida dirigida a Claude.
- Una forma de hacer que el texto del usuario cambie el comportamiento de la skill (inyección de instrucciones).
- Un secreto, un token o datos personales publicados en el repositorio.
- Un problema en los workflows (`.github/workflows/`) o en la cadena de publicación.

## Qué no lo es

- Una traducción o una explicación de inglés incorrecta: abre un issue con la plantilla «Error de traducción o explicación».
- Que la skill no se active en una plataforma: abre un issue con la plantilla de activación.

## Cómo se protege el proyecto

- La skill no lleva scripts ni URLs externas: son solo instrucciones en texto.
- `CODEOWNERS` exige la revisión del mantenedor sobre la skill, las referencias, las instrucciones y los workflows.
- Las actions de GitHub se fijan por SHA, con permisos mínimos por job, y Dependabot las mantiene al día.
- Cada PR pasa por un validador y por una búsqueda de secretos (gitleaks).
- Para volver a una versión anterior: descarga el zip del Release previo o revierte el commit (`git revert`); un parche automático sale en minutos.
