# DUT, señales y jerarquía

**DUT** significa *Device Under Test*: el módulo HDL que queremos verificar.

En los ejercicios, el DUT suele estar en `adder.sv` y el testbench en `adder_tb.py`.

## Acceso a señales

Desde Python se accede a los puertos del módulo con `dut.<señal>`:

```python
dut.a.value = 12
dut.b.value = 15
await Timer(10, units="ns")
resultado = dut.s.value
```

## Puertos e internos

Si el HDL declara:

```systemverilog
module adder(
    input [3:0] a,b,
    output [4:0] s
);
```

el test puede usar:

```python
dut.a.value = 1
dut.b.value = 2
print(dut.s.value)
```

Algunos ejercicios también acceden a señales internas, como clocks generados dentro del DUT. Eso es útil para aprender, aunque en proyectos grandes suele preferirse verificar por la interfaz pública.

## TOPLEVEL

`TOPLEVEL` en el Makefile debe coincidir con el nombre del módulo HDL:

```make
TOPLEVEL := adder
```

Si `TOPLEVEL` no coincide, la simulación no puede encontrar el DUT.
