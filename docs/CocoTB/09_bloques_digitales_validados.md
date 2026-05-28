# Bloques digitales validados

Esta parte del curso verifica varios bloques digitales pequeños. Cada bloque sirve para practicar un concepto de verificación.

## Mux

Un multiplexor selecciona una entrada según `sel`.

Conceptos practicados:

- estímulos sobre entradas
- selección de bits
- chequeo contra resultado esperado

## Sumador

Los sumadores prueban lógica combinacional aritmética.

Conceptos practicados:

- overflow por ancho de bits
- comparación con modelo Python `a + b`
- randomización de operandos

## Priority encoder

Un priority encoder devuelve la posición de la entrada activa con mayor prioridad.

Conceptos practicados:

- representación binaria
- casos borde
- comparación entre vector de entrada y salida codificada

## Flip-flop D

El flip-flop D captura `din` en un flanco de clock.

Conceptos practicados:

- clocks
- reset
- sincronización con `RisingEdge`
- validación de lógica secuencial

## Memoria

La memoria permite escribir y leer direcciones.

Conceptos practicados:

- modelo esperado en Python con diccionario
- secuencia reset, escritura y lectura
- concurrencia entre clock, reset, writer y reader
