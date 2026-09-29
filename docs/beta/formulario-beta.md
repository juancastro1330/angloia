# Formulario de la beta (5 preguntas)

Cópialo en un formulario (Google Forms, Typeform o el que prefieras). Se envía el **día 7** de la beta, después del check-in del día 3. Debe tomar unos 2 minutos.

**Recordatorio para quien responda:** no pegues conversaciones reales ni datos personales.

## Preguntas

**1. ¿Lo sigues teniendo activo?**
( ) Sí  ( ) No  ( ) A veces

**2. Del 1 al 5, ¿qué tan útil te resulta el bloque de inglés?**
1 (nada útil) · 2 · 3 · 4 · 5 (muy útil)

**3. Del 1 al 5, ¿qué tanto te molesta o interrumpe?**
1 (nada) · 2 · 3 · 4 · 5 (mucho)

**4. ¿Qué frase o aprendizaje recuerdas de esta semana?**
*(respuesta corta)*

**5. ¿Qué cambiarías?**
*(respuesta abierta)*

## Datos para el análisis (opcionales)

Ayudan a interpretar los resultados. Pídelos aparte o añádelos al formulario:

- Plan de Claude: Free / Pro / otro.
- Plataforma principal: web / escritorio / móvil / Claude Code.
- Nivel aproximado de inglés: principiante / intermedio / avanzado.
- ¿Programas o trabajas en tecnología? Sí / No.

## Cómo calcular la retención

**Meta:** al menos el **60 %** de los beta testers lo siguen usando a los 7 días.

```
retención = respuestas «Sí» en la pregunta 1  /  beta testers confirmados
```

- Quien **no responde** cuenta como «No», para no inflar el resultado.
- «A veces» **no** cuenta como retenido, pero se reporta aparte: es una señal de fatiga y de que quizá conviene bajar la frecuencia por defecto.
- Ejemplo: de 8 confirmados, 5 responden «Sí», 1 «A veces» y 2 no responden → 5 / 8 = **62,5 %**. Se alcanza la meta.

Esta definición es una propuesta; si prefieres contar «A veces» como media, cámbiala **antes** de mirar los resultados.

## Cómo leer las respuestas

| Señal | Qué hacer |
|---|---|
| Pregunta 3 alta (4 o 5) en varias personas | Bajar la frecuencia por defecto o acortar el modo ligero |
| Pregunta 2 baja (1 o 2) | Revisar qué aprendizajes se eligen y si son relevantes |
| Pregunta 4 vacía o vaga | El aprendizaje no se queda: reforzar el reto y el resumen |
| Traducciones incorrectas mencionadas en la pregunta 5 | Prioridad máxima: corregir y añadir un ejemplo en `evals/` |
