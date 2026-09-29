# 🇺🇸 AngloIA (English tutor for Spanish speakers)

**Learn English while you use Claude for everything else.** You write in Spanish, as usual. Claude solves your request and, at the end, teaches you how to say your own message in English.

*AngloIA = "Anglo" (English) + "IA", the Spanish acronym for AI.*

[![CI](https://github.com/juancastro1330/angloia/actions/workflows/ci.yml/badge.svg)](https://github.com/juancastro1330/angloia/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[Versión en español](README.md)

## Before and after

> **You:** ¿Me ayudas a organizar mi semana? Tengo muchas reuniones. *(Can you help me organize my week? I have a lot of meetings.)*
>
> *(Claude helps you plan your week…)*
>
> **🇺🇸 Así lo dirías en inglés:** "Can you help me organize my week? I have a lot of meetings."
> **🔑 Frases clave:** *organize my week* · *a lot of*
> **⚠️ Ojo:** don't say "many reunions". *Reunion* means a get-together after time apart; a work *reunión* is a *meeting*.

It is not a translator. Its value is **active learning**: challenges so you try first, corrections of your English, repetition of your recurring mistakes and a summary of your best phrases.

The tutor's notes are written in Spanish on purpose: the audience is Spanish speakers.

## How it works: two layers

| Layer | What it is | For whom |
|---|---|---|
| **1. Instructions for Claude** | A short text you paste once into your account. It applies to **every** chat | Everyone. The recommended way to start |
| **2. The `angloia` skill** | Adds the full format, the modes and 4 deep references (false friends, prepositions, tenses and levels) | Anyone who wants the best quality |

The skill improves the result but is **not required**: the instructions make sure the tutor always acts.

## Installation

| Platform | How to install |
|---|---|
| **Any plan (recommended to start)** | Paste the text from [`instrucciones/instrucciones-claude.md`](instrucciones/instrucciones-claude.md) into "Instructions for Claude" |
| **claude.ai web and desktop** | Download [`angloia.zip`](https://github.com/juancastro1330/angloia/releases/latest/download/angloia.zip) from the latest Release and upload it in the Skills section (code execution must be enabled) |
| **Mobile apps** | They use whatever is installed on your account |
| **Claude Code** | `/plugin marketplace add juancastro1330/angloia` and then `/plugin install angloia@angloia` |
| **Official directory** | Install it from Claude's directory once the plugin is approved (it updates itself) |

> Does your free plan show the Skills section? The official documentation is not fully clear and it depends on your account. If you don't see it, use the instructions: they work the same on any plan.

`angloia` is the name of the skill, the plugin and the repository.

## How to use it

Write in Spanish as usual. A short English block appears at the end of each reply. Change the behavior with these commands (they are in Spanish because the users are Spanish speakers):

| Command | What it does |
|---|---|
| *(nothing, default)* **Light mode** | One phrase from your message in English and one thing to learn |
| `modo completo` | Your whole message in English, 2 or 3 key phrases and one typical trap |
| `modo reto` | Asks you to translate one of your own phrases, then corrects you. It also appears on its own roughly every 4 or 5 messages |
| `modo conversación` | Replies entirely in simple English, matched to your level |
| `modo ligero` | Back to the default mode |
| `pausa inglés` / `sigue inglés` | Pause and resume the tutor |
| `inglés siempre` / `inglés a veces` / `inglés solo si pido` | Change how often the block appears |
| `mi nivel es B1` | Set your level (A1 to C2); otherwise it is inferred |
| `resumen` | Gives you "Mis 3 frases de hoy" to save or screenshot |

**When there is no block:** very short messages ("ok", "gracias"), crisis, health, grief or emergency topics, and while paused. In long messages only the 1 or 2 most useful sentences are translated, and if the reply is mostly code the block shrinks to one line.

**When you write in English**, it corrects at most 2 mistakes per message (the ones that hurt understanding most), with the natural version and a short reason in Spanish. If it is unclear whether something is a mistake, it doesn't correct it. US and UK English are both accepted; US English is taught by default. Regionalisms are understood, not corrected.

## Privacy and security

- **It publishes nobody's conversations.** Only the skill's code is public.
- The skill contains no scripts and no external links. It is plain text instructions.
- Examples in this repository are made up; real conversations are never used.
- Whatever you type is treated as material to translate, never as commands that change the tutor's rules.
- To report a security issue, see [`SECURITY.md`](SECURITY.md).

## Compatibility

Last reviewed: **September 29, 2026**. Claude's platforms change often, so this repository reviews compatibility monthly. Per-platform status is in [`docs/compatibilidad.md`](docs/compatibilidad.md).

## Contributing

Contributions are welcome: new false friends, examples, test cases and fixes. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) (in Spanish). If you find an incorrect translation or explanation, open an issue with the matching template.

```bash
python3 scripts/validate.py                                  # validate the skill, manifests and evals
python3 -m unittest discover -s scripts -p "test_*.py" -v    # test the validator
python3 scripts/build_zips.py                                # build dist/angloia.zip and dist/angloia-plugin.zip
```

## License and notice

[MIT](LICENSE) license.

**This is a community project and is not affiliated with Anthropic.** "Claude" is a trademark of Anthropic.
