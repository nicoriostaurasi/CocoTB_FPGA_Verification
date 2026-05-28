# Entorno de simulación

El entorno de simulación combina tres piezas:

- **Python**: ejecuta el testbench cocotb.
- **cocotb**: conecta Python con el simulador HDL.
- **Icarus Verilog**: compila y simula el módulo Verilog/SystemVerilog.

En este proyecto el entorno está encapsulado en Docker para evitar diferencias entre Windows y Linux. Ver también [[10_debug_waveforms_y_vcd|Debug con waveforms y VCD]].

## Ejecutar dentro del contenedor

Desde la raíz del repositorio:

```powershell
docker compose run --rm cocotb bash
```

Dentro del contenedor:

```sh
cd /work/part_02/section_01/01_generation_signals
make clean
make icarus=sim
```

`/work` es el repositorio montado dentro del contenedor.

## Por qué usar make clean

Icarus genera archivos intermedios en `sim_build/`, especialmente `sim.vvp`. Si ese archivo fue generado con otra versión de Icarus, puede aparecer un error como:

```text
VVP input file 12.0 can not be run with run time version 11.0
```

La solución es limpiar antes de simular:

```sh
make clean
make icarus=sim
```

## Rol del Makefile

Cada ejercicio tiene un `Makefile` con variables de cocotb:

```make
TOPLEVEL_LANG ?= verilog
SIM ?= icarus
VERILOG_SOURCES = $(shell pwd)/adder.sv
TOPLEVEL := mux
MODULE   := adder_tb
include $(shell cocotb-config --makefiles)/Makefile.sim
```

- `SIM`: simulador usado.
- `VERILOG_SOURCES`: archivos HDL que se compilan.
- `TOPLEVEL`: módulo top de `adder.sv`.
- `MODULE`: archivo Python del testbench, sin `.py`.
