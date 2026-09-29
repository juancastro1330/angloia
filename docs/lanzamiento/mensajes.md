# Mensajes de lanzamiento por canal

Borradores para el lanzamiento escalonado (días 19 a 21 del plan), en el **orden de la tabla**. Cambia lo que haga falta para que suene a ti.

## Antes de publicar cualquier cosa

- [ ] Existe el Release **v1.0.0** con `profe-ingles.zip` y el enlace directo del README funciona.
- [ ] El README tiene el GIF de antes y después en los primeros 5 segundos.
- [ ] La retención de la beta llegó al 60 % y no quedan errores graves de traducción sin corregir.
- [ ] El aviso de **no afiliación con Anthropic** está en el README y aparece en cada pieza.

**Regla para todos los mensajes:** no publiques cifras, testimonios ni capturas que no tengas. Donde ves `[…]`, pon un dato **real** de tu beta o quita la frase. No uses conversaciones reales de nadie; enseña ejemplos inventados.

Enlaces a reemplazar: `[REPO]` = https://github.com/juancastro1330/skill-ingles · `[ZIP]` = https://github.com/juancastro1330/skill-ingles/releases/latest/download/profe-ingles.zip · `[VIDEO]` = el enlace del video de 60 s.

---

## 1. Beta testers

**Por qué primero:** son tus primeras estrellas y testimonios. **Qué pedir:** que lo compartan si les sirvió, no que lo hagan por compromiso.

> Ya salió Profe Inglés 🎉 Gracias por probarlo cuando todavía tenía aristas. Con lo que me contaste cambié [algo concreto que cambiaste por sus notas].
>
> Si te sirvió, compártelo con alguien que esté aprendiendo inglés, o dale una ⭐ al repo: [REPO]. Si algo no te gustó, dímelo también, que eso me ayuda más.

---

## 2. Creadores de inglés y comunidades hispanas

**Por qué:** es el público real: gente que aprende inglés y no programa. **Formato principal:** el video de 60 s (guion en [`../beta/guion-video-60s.md`](../beta/guion-video-60s.md)).

### Mensaje directo a creadores

> Hola [nombre], sigo tu contenido de inglés y quería enseñarte algo. Hice una herramienta gratuita y de código abierto que convierte cualquier chat con Claude en una mini clase de inglés: escribes en español, Claude resuelve lo tuyo y al final te enseña cómo decirlo en inglés, con retos para que lo intentes tú primero.
>
> Aquí hay un video de 1 minuto: [VIDEO]. Se instala pegando un texto, sin código. Es un proyecto comunitario, no afiliado a Anthropic. No te pido nada a cambio; si te parece útil para tu comunidad, encantado de resolverte cualquier duda.

### Texto para acompañar el video (TikTok, Reels, Shorts)

> ¿Y si aprendieras inglés mientras haces lo de siempre? 👇
> Escribes en español, Claude te ayuda y al final te enseña cómo decirlo en inglés. Gratis y de código abierto. Instalación en 1 minuto, sin programar.
> Enlace en el perfil. #inglés #aprenderinglés #claude
> (Proyecto comunitario, no afiliado a Anthropic)

**Comentario fijado:** «Enlace y pasos: [REPO]. Si un día no quieres inglés, escribes "pausa inglés" y listo.»

### Grupos de WhatsApp, Telegram, Facebook y Discord

Cada grupo tiene sus normas. Pide permiso al administrador antes de publicar.

> Comparto algo que hice por si le sirve a alguien: Profe Inglés, una herramienta gratuita que convierte tus chats con Claude en clases cortas de inglés. Escribes en español y al final de cada respuesta te enseña cómo decir tu mensaje en inglés. Video de 1 minuto y pasos: [REPO]
> Es de código abierto y no está afiliada a Anthropic. Si la prueban, me encantaría saber qué les parece.

---

## 3. Reddit: r/ClaudeAI, r/EnglishLearning y r/languagelearning

**Antes de publicar en cada uno:** lee las reglas de autopromoción del subreddit y cumple sus requisitos (etiquetas, días permitidos, historial de participación). **No pegues el mismo texto en los tres.** Sé transparente: es tu proyecto. Pide opiniones, no estrellas.

### r/ClaudeAI (ángulo: una skill útil y cómo está armada)

**Título:** `I built an open-source Claude skill that turns any chat into a short English lesson for Spanish speakers`

> I'm a Spanish speaker and I wanted to learn English without adding another app to my day, so I made Profe Inglés. You keep writing to Claude in Spanish; it solves your request first, and at the end it shows how to say *your own message* in English, with a key phrase and a common trap (false friends, prepositions). It also runs short challenges ("translate this sentence of yours") and corrects your English, at most 2 mistakes at a time.
>
> It has two layers: a short text for Claude's custom instructions (works on any plan) and a skill with deeper references. The skill has no scripts and no external URLs; user text is treated as material to translate, never as commands.
>
> Repo (MIT): [REPO]. It's a community project, not affiliated with Anthropic. I'd love feedback on the false friends list and on whether the block gets tiring.

### r/EnglishLearning y r/languagelearning (ángulo: aprendizaje activo, no otro traductor)

**Título:** `A free tool that makes you try first: learn English while you use an AI assistant in Spanish`

> The idea: reading a translation of your own message is passive. This tool adds active practice on top of your normal chats: challenges (you translate first, then it corrects you), a "3 phrases of the day" summary and, when the assistant's memory keeps them, a revisit of your recurring mistakes days later. The notes are written in Spanish, since it's made for Spanish speakers. CEFR levels A1–C2, US English by default and it accepts British.
>
> It's free and open source: [REPO]. It runs on top of an AI assistant (Claude), so it's a fit if you already use one. I'm looking for feedback from learners and teachers, especially about the corrections and the level adaptation.

*(El repaso espaciado como tal es de la v2. En la v1 solo se retoman errores si la memoria del asistente los conserva; no prometas más que eso.)*

---

## 4. Pull requests a las 3 listas awesome-claude-skills

**Qué:** una línea de descripción por lista. **Antes de cada PR:** abre el `CONTRIBUTING` de la lista y respeta su formato, su orden alfabético y su sección. No inventes categorías.

Línea sugerida (en inglés, que es el idioma de esas listas):

```markdown
- [profe-ingles](https://github.com/juancastro1330/skill-ingles) - English tutor for Spanish speakers: solves your request first, then teaches how to say your own message in English (light, full, challenge and conversation modes, CEFR A1–C2).
```

**Título del PR:** `Add profe-ingles (English tutor for Spanish speakers)`

**Cuerpo del PR:**

> Adds profe-ingles, an open-source (MIT) skill that turns any chat into a short English lesson for Spanish speakers. Two layers: pasteable custom instructions (any plan) and a skill with references. No scripts, no external URLs in the skill. Not affiliated with Anthropic.

---

## 5. Show HN, X y LinkedIn (ángulo técnico)

**Canal secundario.** El ángulo es la **arquitectura de dos capas**: las instrucciones son el producto y la skill es la mejora.

### Show HN

**Título:** `Show HN: Profe Inglés – an English tutor for Spanish speakers, as a Claude skill`

> I made a small open-source tutor that rides on top of Claude. The interesting part was the architecture. A skill is activated by relevance and might not exist on every plan, so I inverted it: the primary product is a ~1,700-character block of custom instructions that applies to every chat on any plan, and the skill is an enhancement (full formats, four reference files, CEFR levels).
>
> A few design decisions that might be useful to others: the skill has no scripts and no URLs, so a text change is the only attack surface, which is why CODEOWNERS covers it like code; user text is explicitly treated as material to translate, not commands; and CI validates the skill's limits (name, description length, body under 500 lines, links to references) and fails on any of them. Actions are pinned by SHA and releases are automated.
>
> It is a community project, not affiliated with Anthropic. Repo: [REPO]. I'd like to hear how you'd evaluate a skill like this beyond checking that it activates.

### X (hilo de 5 posts)

1. `Hice una herramienta gratis para aprender inglés mientras usas Claude: escribes en español, resuelve lo tuyo y al final te enseña cómo decir tu mensaje en inglés. 🧵`
2. `No es un traductor: tiene retos (lo intentas tú primero), corrige tu inglés (máx. 2 errores a la vez) y un resumen con tus 3 frases del día.`
3. `Se instala pegando un texto en "Instrucciones para Claude". Funciona en cualquier plan. Si tu cuenta tiene Skills, también hay una versión con más referencias.`
4. `Es de código abierto (MIT) y sin scripts ni enlaces externos: solo texto. Proyecto comunitario, no afiliado a Anthropic.`
5. `Video de 1 minuto y código: [REPO]`

### LinkedIn (en español)

> Aprender inglés suele fallar por un motivo simple: no encaja en el día. Por eso hice Profe Inglés.
>
> Escribes en español a Claude, como siempre. Resuelve tu consulta y, al final, te enseña cómo decir **tu propio mensaje** en inglés. De vez en cuando te pide que lo intentes tú primero y te corrige.
>
> Lo publiqué como proyecto abierto (MIT): [REPO]. Es una iniciativa comunitaria, no afiliada a Anthropic. [Una frase real sobre lo que aprendiste en la beta.]
>
> Si enseñas inglés o aprendes, me sirve mucho tu opinión.

---

## Después de publicar

- Responde cada comentario en las primeras horas; es lo que más pesa en Reddit y en HN.
- Anota en un issue o en una nota los errores de traducción que reporten: son de prioridad máxima.
- No pidas votos ni estrellas en los canales donde las normas lo prohíben.
