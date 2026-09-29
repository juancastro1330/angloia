# Good first issues (borradores)

Diez tareas pequeñas y bien acotadas para quien contribuye por primera vez. El día 16 del plan se crean como issues con la etiqueta `good first issue`; aquí están redactadas para copiarlas tal cual.

**Ya están creados como issues** (29 de septiembre de 2026): [#1](https://github.com/juancastro1330/angloia/issues/1), [#2](https://github.com/juancastro1330/angloia/issues/2), [#3](https://github.com/juancastro1330/angloia/issues/3), [#4](https://github.com/juancastro1330/angloia/issues/4), [#5](https://github.com/juancastro1330/angloia/issues/5), [#6](https://github.com/juancastro1330/angloia/issues/6), [#7](https://github.com/juancastro1330/angloia/issues/7), [#8](https://github.com/juancastro1330/angloia/issues/8), [#9](https://github.com/juancastro1330/angloia/issues/9) y [#10](https://github.com/juancastro1330/angloia/issues/10). Los números siguen el orden de este documento. Si cambias el texto de un borrador, cambia también su issue.

Antes de empezar cualquiera: lee [`CONTRIBUTING.md`](../CONTRIBUTING.md) y corre `python3 scripts/validate.py`.

---

## 1. Añadir 10 falsos amigos a `false-friends.md`

**Qué:** amplía `plugins/angloia/skills/angloia/references/false-friends.md` con 10 falsos amigos nuevos que no estén ya en la tabla.
**Cómo:** cada fila lleva lo que se quiere decir, la trampa, lo que esa palabra significa realmente y la forma correcta. Verifica cada palabra en un diccionario fiable (Cambridge, Oxford, Merriam-Webster) y cita cuál en la descripción del PR.
**Listo cuando:** `validate.py` pasa y cada fila está verificada.
**Título del PR:** `feat: añade 10 falsos amigos`

## 2. Escribir 5 ejemplos de nivel A1

**Qué:** añade 5 ejemplos nuevos de nivel A1 a `evals/golden-examples.md` (G31 a G35).
**Cómo:** sigue el formato de los ejemplos existentes. Mensajes inventados, frases cortas, vocabulario básico.
**Listo cuando:** `validate.py` pasa y el inglés esperado es de A1.
**Título del PR:** `test: añade 5 ejemplos de nivel A1`

## 3. Ampliar los casos de activación

**Qué:** añade 5 casos más a «No deben activar» y 5 a «Deben activar» en `evals/activation.md`.
**Cómo:** piensa en mensajes ambiguos: inglés técnico, otros idiomas, comandos, mezcla de idiomas.
**Listo cuando:** los IDs siguen la numeración (A21…, N11…) y `validate.py` pasa.
**Título del PR:** `test: amplía los casos de activación`

## 4. Añadir los 30 verbos irregulares más frecuentes

**Qué:** añade a `references/tenses.md` una tabla con los 30 verbos irregulares más frecuentes (infinitivo, pasado, participio y significado).
**Cómo:** ordénalos por frecuencia y verifica cada forma.
**Listo cuando:** la tabla está completa y el cuerpo de `SKILL.md` no cambia.
**Título del PR:** `feat: añade verbos irregulares frecuentes`

## 5. Revisar la traducción de `README.en.md`

**Qué:** revisa que el inglés de `README.en.md` sea natural y que diga lo mismo que `README.md`.
**Cómo:** compara sección por sección y corrige lo que suene literal o distinto.
**Listo cuando:** ambas versiones dicen lo mismo y los enlaces funcionan.
**Título del PR:** `docs: mejora la traducción del README en inglés`

## 6. Regionalismos de Chile, Perú y Venezuela

**Qué:** añade 3 ejemplos (uno por país) a `evals/golden-examples.md` con regionalismos frecuentes que el tutor debe entender sin corregir.
**Cómo:** mensajes inventados; el bloque esperado traduce el significado con naturalidad.
**Listo cuando:** cada ejemplo indica el país y explica el regionalismo en «Criterios».
**Título del PR:** `test: añade regionalismos de Chile, Perú y Venezuela`

## 7. Casos límite nuevos

**Qué:** añade 3 casos límite a `evals/edge-cases.md` (E21 a E23).
**Cómo:** ideas: un mensaje con varias listas, una tabla pegada, un mensaje que mezcla tres idiomas.
**Listo cuando:** cada caso tiene «Entrada» y «Esperado», y `validate.py` pasa.
**Título del PR:** `test: añade casos límite`

## 8. Mejorar los mensajes de error del validador

**Qué:** revisa los mensajes de `scripts/validate.py` y haz que cada uno diga qué archivo falla y cómo arreglarlo.
**Cómo:** ejecuta el validador con errores provocados a propósito y compara.
**Listo cuando:** las pruebas de `scripts/test_validate.py` siguen pasando.
**Título del PR:** `fix: mejora los mensajes del validador`

## 9. Prueba nueva para el validador

**Qué:** añade una prueba a `scripts/test_validate.py` para un caso que aún no cubre. Por ejemplo, un `SKILL.md` con `allowed-tools` (debe aceptarse) o con la clave `name` repetida (debe fallar).
**Cómo:** sigue el estilo de las pruebas existentes.
**Listo cuando:** la prueba falla si rompes la regla y pasa si no.
**Título del PR:** `test: cubre un caso nuevo del validador`

## 10. Guía paso a paso para probar la skill en Claude Code

**Qué:** escribe `docs/probar-en-claude-code.md`: cómo instalar el plugin desde el marketplace, cómo comprobar que se activa y cómo correr los casos de `evals/`.
**Cómo:** con capturas o comandos exactos, para alguien que nunca ha usado Claude Code. Enlázala desde `README.md`.
**Listo cuando:** una persona ajena al proyecto la sigue sin ayuda y `validate.py` pasa (comprueba los enlaces).
**Título del PR:** `docs: añade guía para probar en Claude Code`
