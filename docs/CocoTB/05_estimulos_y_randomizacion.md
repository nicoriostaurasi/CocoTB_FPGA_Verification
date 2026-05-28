# Estímulos y randomización

Un estímulo es cualquier valor que el testbench aplica al DUT.

## Estímulos fijos

Sirven para entender el circuito y probar casos simples:

```python
dut.a.value = 12
dut.b.value = 15
await Timer(10, units="ns")
```

## Estímulos aleatorios

La randomización permite explorar más combinaciones:

```python
a = random.randint(0, 15)
b = random.randint(0, 15)
dut.a.value = a
dut.b.value = b
```

Esto aparece en muxes, sumadores, priority encoders y memoria.

## Rango correcto

El rango debe respetar el ancho de la señal:

- 1 bit: `0` a `1`
- 4 bits: `0` a `15`
- 8 bits: `0` a `255`

Si se aplican valores fuera de rango, el simulador puede truncarlos y ocultar errores del test.

## Estímulo dirigido vs aleatorio

- **Dirigido**: prueba casos elegidos a mano, como borde inferior, borde superior u overflow.
- **Aleatorio**: explora muchas combinaciones sin escribir cada caso manualmente.

Un buen test suele combinar ambos.
