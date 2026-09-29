# 🇺🇸 Profe Inglés

**Aprende inglés mientras usas Claude para lo de siempre.** Escribes en español, como siempre. Claude resuelve tu consulta y, al final, te enseña cómo decir tu propio mensaje en inglés.

[![CI](https://github.com/juancastro1330/skill-ingles/actions/workflows/ci.yml/badge.svg)](https://github.com/juancastro1330/skill-ingles/actions/workflows/ci.yml)
[![Licencia: MIT](https://img.shields.io/badge/licencia-MIT-blue.svg)](LICENSE)

[English version](README.en.md)

<!-- Día 17 (mantenedor): añadir aquí el GIF de antes y después: docs/demo.gif -->

## Antes y después

> **Tú:** ¿Me ayudas a organizar mi semana? Tengo muchas reuniones.
>
> *(Claude te ayuda con tu semana…)*
>
> **🇺🇸 Así lo dirías en inglés:** "Can you help me organize my week? I have a lot of meetings."
> **🔑 Frases clave:** *organize my week* (organizar mi semana) · *a lot of* (muchos/as)
> **⚠️ Ojo:** no digas "many reunions". *Reunion* es un reencuentro; una reunión de trabajo es *meeting*.

No es un traductor. Su valor está en el **aprendizaje activo**: retos para que lo intentes tú, corrección de tu inglés, repetición de tus errores y un resumen de tus mejores frases.

## Cómo funciona: dos capas

| Capa | Qué es | Para quién |
|---|---|---|
| **1. Instrucciones para Claude** | Un texto corto que pegas una vez en tu cuenta. Se aplica a **todos** tus chats | Todos. Es la forma recomendada de empezar |
| **2. La skill `profe-ingles`** | Añade el formato completo, los modos y 4 referencias profundas (falsos amigos, preposiciones, tiempos verbales y niveles) | Quien quiera la mejor calidad |

La skill mejora el resultado, pero **no es imprescindible**: las instrucciones garantizan que el tutor actúe siempre.

## Instalación

| Plataforma | Cómo se instala |
|---|---|
| **Cualquier plan (recomendado para empezar)** | Pega el texto de [`instrucciones/instrucciones-claude.md`](instrucciones/instrucciones-claude.md) en «Instrucciones para Claude» |
| **claude.ai web y escritorio** | Descarga [`profe-ingles.zip`](https://github.com/juancastro1330/skill-ingles/releases/latest/download/profe-ingles.zip) del último Release y súbelo en la sección de Skills (requiere la ejecución de código activada) |
| **Apps móviles** | Usan lo que hayas instalado en tu cuenta |
| **Claude Code** | `/plugin marketplace add juancastro1330/skill-ingles` y luego `/plugin install profe-ingles@profe-ingles` |
| **Directorio oficial** | Instálala desde el directorio de Claude cuando el plugin sea aprobado (se actualiza sola) |

> ¿Tu plan gratuito muestra la sección de Skills? La documentación oficial no lo aclara del todo y depende de tu cuenta. Si no la ves, usa las instrucciones: funcionan igual en cualquier plan.

`profe-ingles` es el nombre de la skill y del plugin; el repositorio se llama `skill-ingles`.

## Cómo se usa

Escribe en español con normalidad. Al final de cada respuesta aparece un bloque breve de inglés. Puedes cambiar el comportamiento con estos comandos:

| Comando | Qué hace |
|---|---|
| *(nada, por defecto)* **Modo ligero** | Una frase de tu mensaje en inglés y un aprendizaje |
| `modo completo` | Tu mensaje en inglés, 2 o 3 frases clave y una trampa típica |
| `modo reto` | Te pide traducir una frase tuya y luego te corrige. También sale solo, más o menos cada 4 o 5 mensajes |
| `modo conversación` | Responde todo en inglés sencillo, adaptado a tu nivel |
| `modo ligero` | Vuelve al modo por defecto |
| `pausa inglés` / `sigue inglés` | Pausa y reanuda el tutor |
| `inglés siempre` / `inglés a veces` / `inglés solo si pido` | Cambia la frecuencia del bloque |
| `mi nivel es B1` | Fija tu nivel (A1 a C2); si no lo dices, lo infiere |
| `resumen` | Te da «Mis 3 frases de hoy» para guardar o capturar |

**Cuándo no aparece el bloque:** en mensajes muy cortos («ok», «gracias»), en temas de crisis, salud, duelo o emergencia, y con la pausa activada. En mensajes largos traduce solo las 1 o 2 frases más útiles, y si tu respuesta es sobre todo código, reduce el bloque a una línea.

**Cuando escribes en inglés**, corrige como máximo 2 errores por mensaje (los que más impiden entender), con la versión natural y un porqué en español. Si hay duda de que algo sea un error, no lo corrige. Acepta inglés de EE. UU. y del Reino Unido; enseña el de EE. UU. por defecto. Entiende tus regionalismos sin corregirlos.

## Privacidad y seguridad

- **No publica conversaciones de nadie.** Solo es público el código de la skill.
- La skill no lleva scripts ni enlaces externos. Son solo instrucciones en texto.
- Los ejemplos del repositorio están inventados; nunca se usan conversaciones reales.
- El texto que escribes se trata como material para traducir, nunca como órdenes que cambien las reglas del tutor.
- Para reportar un problema de seguridad, mira [`SECURITY.md`](SECURITY.md).

## Compatibilidad

Última revisión: **29 de septiembre de 2026**. Las plataformas de Claude cambian con frecuencia, por eso este repositorio revisa la compatibilidad cada mes. El estado por plataforma está en [`docs/compatibilidad.md`](docs/compatibilidad.md).

## Contribuir

Las contribuciones son bienvenidas: falsos amigos nuevos, ejemplos, casos de prueba y correcciones. Empieza por [`CONTRIBUTING.md`](CONTRIBUTING.md). Si encuentras una traducción o una explicación incorrecta, abre un issue con la plantilla correspondiente.

```bash
python3 scripts/validate.py                                  # valida la skill, los manifiestos y las evals
python3 -m unittest discover -s scripts -p "test_*.py" -v    # prueba el validador
python3 scripts/build_zips.py                                # genera dist/profe-ingles.zip y dist/profe-ingles-plugin.zip
```

## Licencia y aviso

Licencia [MIT](LICENSE).

**Este es un proyecto comunitario y no está afiliado a Anthropic.** «Claude» es una marca de Anthropic.
