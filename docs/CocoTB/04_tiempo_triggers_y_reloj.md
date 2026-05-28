# Tiempo, triggers y reloj

cocotb controla la simulación con eventos llamados **triggers**. Un trigger suspende la corrutina hasta que el simulador llegue a cierta condición.

## Timer

`Timer` espera una cantidad fija de tiempo de simulación:

```python
await Timer(10, units="ns")
```

Se usa en ejercicios de estímulo simple y delays combinacionales.

## Flancos

Para lógica secuencial se esperan flancos de reloj:

```python
await RisingEdge(dut.clk)
await FallingEdge(dut.clk)
```

Esto sincroniza el testbench con el DUT.

## ClockCycles

`ClockCycles` espera una cantidad de ciclos:

```python
await ClockCycles(dut.clk, 5)
```

Es más expresivo que repetir cinco veces `RisingEdge`.

## Relojes generados desde cocotb

cocotb puede generar clocks:

```python
cocotb.start_soon(Clock(dut.clk, 10, "ns").start())
```

Esto crea un reloj de periodo 10 ns. Ver [[08_concurrencia_en_cocotb|Concurrencia en cocotb]] para entender por qué se usa `start_soon`.

## Relojes generados en HDL

Algunos ejercicios generan clock dentro del Verilog:

```systemverilog
reg clk = 0;
always #10 clk = ~clk;
```

Esto es útil para practicar triggers, pero en verificación real suele ser más flexible generar clocks desde el testbench.
