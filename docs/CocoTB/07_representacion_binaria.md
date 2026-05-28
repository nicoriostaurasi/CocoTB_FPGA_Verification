# Representación binaria

Los testbenches trabajan con valores que pueden verse como enteros, binarios o vectores de bits.

## `.value`

`dut.signal.value` es el valor cocotb de una señal HDL:

```python
dout = dut.dout.value
```

Para convertirlo a entero:

```python
dout_int = dut.dout.value.integer
```

## BinaryValue

Algunos ejercicios usan:

```python
from cocotb.binary import BinaryValue
```

`BinaryValue` permite manipular bits y obtener strings binarios:

```python
din_bin = BinaryValue(value=0, n_bits=8, bigEndian=False)
din_bin.integer = 13
print(din_bin.binstr)
```

## Endianness

`bigEndian=False` afecta cómo se indexa la representación binaria. Este punto es importante en muxes de bits, donde el test selecciona un bit específico de un vector.

## Recomendación didáctica

Para ejercicios simples:

- usar enteros para estímulos y comparaciones aritméticas
- usar `BinaryValue` cuando el objetivo sea mirar o seleccionar bits
