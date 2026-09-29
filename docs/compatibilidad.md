# Compatibilidad

**Última revisión: 29 de septiembre de 2026.** Se revisa cada mes, y también cuando cambie algo importante en las plataformas de Claude.

> **Estado: sin verificar.** Esta tabla se rellena con las pruebas reales del plan (semana 2). Hasta entonces, ninguna plataforma está confirmada. La documentación oficial no aclara del todo si el plan gratuito incluye Skills, así que hay que comprobarlo en una cuenta real.

## Estado por plataforma

Cómo probar cada celda: instala la capa, abre un chat nuevo y corre los 30 casos de [`evals/activation.md`](../evals/activation.md) y los 30 ejemplos de [`evals/golden-examples.md`](../evals/golden-examples.md).

| Plataforma | Capa 1: instrucciones | Capa 2: skill | Fecha de la prueba | Notas |
|---|---|---|---|---|
| claude.ai (web) | Por verificar | Por verificar | | |
| Claude para escritorio | Por verificar | Por verificar | | |
| App móvil (iOS) | Por verificar | Por verificar | | Usa lo instalado en la cuenta |
| App móvil (Android) | Por verificar | Por verificar | | Usa lo instalado en la cuenta |
| Claude Code | No aplica | Por verificar | | Vía `/plugin marketplace add juancastro1330/skill-ingles` |
| Directorio oficial | No aplica | Pendiente de envío | | Tras el Release 1.0.0 |

Valores posibles: **Funciona**, **Con limitaciones** (anota cuáles), **No funciona**, **Por verificar**.

## Por plan

| Plan | ¿Ve la sección de Skills? | ¿Requiere ejecución de código? | Notas |
|---|---|---|---|
| Free | Por verificar | Por verificar | La capa 1 funciona en cualquier plan |
| Pro | Por verificar | Por verificar | |

## Resultados de las pruebas

| Fecha | Versión | Plataforma | Activación (de 30) | Ejemplos correctos (de 30) | Errores graves | Aprobado |
|---|---|---|---|---|---|---|
| | | | | | | |

**Aprobación:** activación de al menos 27 de 30 (90 %), ejemplos sin ningún error grave, y casos límite sin romperse. Si algo falla, anota la limitación en «Notas»: el plan exige que funcione en todas las plataformas **o** que la limitación quede documentada.
