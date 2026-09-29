# Evals de activación (20 + 10)

Mide si la skill se activa cuando debe y solo cuando debe. Aplica a la **capa 2** (la skill). Las instrucciones de la capa 1 no dependen de esto porque están siempre presentes.

## Cómo correrlos

1. Instala la skill y abre un **chat nuevo** para cada mensaje (así ninguna conversación previa influye).
2. Envía el mensaje tal cual.
3. Marca ✔ si el resultado coincide con lo esperado (activa o no activa), ✘ si no.
4. Anota el resultado en la tabla del final.

**Aprobación: al menos 90 % de aciertos**, es decir, **27 de 30** o más.

Todos los mensajes están inventados.

## Deben activar (20)

Entrada en español, preguntas de inglés y comandos.

- **A01** — «¿Me ayudas a organizar mi semana? Tengo muchas reuniones.»
- **A02** — «Escríbeme un correo para pedir vacaciones.»
- **A03** — «¿Cómo se dice "estoy harto" en inglés?»
- **A04** — «Corrige este texto en inglés: "I am agree with you and I have 30 years."»
- **A05** — «¿Cuál es la diferencia entre *make* y *do*?»
- **A06** — «Explícame el present perfect con ejemplos.»
- **A07** — «Dame ideas de regalo para el cumpleaños de mi mamá.»
- **A08** — «Resume este artículo en cinco puntos: [texto]»
- **A09** — «Tengo un error en mi código de Python, ¿me ayudas a encontrarlo?»
- **A10** — «modo reto»
- **A11** — «pausa inglés»
- **A12** — «Dame el resumen de mis frases de hoy.»
- **A13** — «¿Qué significa "break a leg"?»
- **A14** — «Mi nivel es B1, ¿me explicas los condicionales?»
- **A15** — «Necesito practicar inglés para una entrevista de trabajo.»
- **A16** — «¿"Actually" significa "actualmente"?»
- **A17** — «Tradúceme al inglés: "Nos vemos mañana a las nueve".»
- **A18** — «Quiero un plan para aprender inglés en seis meses.»
- **A19** — «Hola, buenos días.» *(se activa, pero por la regla de mensajes cortos no muestra bloque)*
- **A20** — «¿Cómo se pronuncia "thorough"?»

## No deben activar (10)

Mensajes que no son de un hispanohablante ni piden inglés.

- **N01** — «Refactor this function to use async/await instead of callbacks.»
- **N02** — «Draft a polite email declining a meeting invitation.»
- **N03** — «Peux-tu m'aider à organiser mon voyage à Lyon ?»
- **N04** — «Você pode me ajudar a revisar este código em JavaScript?»
- **N05** — «How do I conjugate the verb "ser" in Spanish?» *(un angloparlante aprendiendo español: dirección opuesta)*
- **N06** — «Translate "good morning" into French and German.»
- **N07** — «Summarize the main causes of the French Revolution in five bullet points.»
- **N08** — Solo un bloque de código o de configuración JSON, sin texto alrededor.
- **N09** — «Kannst du mir bei meiner Bewerbung helfen?»
- **N10** — «What is the difference between a mutex and a semaphore?»

## Resultados

Copia esta tabla en un issue o en `docs/compatibilidad.md` con cada ronda de pruebas.

| Fecha | Versión | Plataforma | Activan (de 20) | No activan (de 10) | Total | Aprobado (≥ 27) |
|---|---|---|---|---|---|---|
| | | | | | | |

**Fallos:** anota el ID (por ejemplo A16 o N05), qué pasó y qué ajuste de la `description` propones. Cada cambio en la `description` obliga a repetir estos 30 casos completos.
