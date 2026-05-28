# Mapa de ejercicios

Este mapa sigue la estructura de `part_02`.

## Section 01

- `01_generation_signals`: generación de señales desde cocotb.
- `02_logging_variables`: uso de logs y observación de variables.

## Section 02

- `01_dut_py`: primer contacto con `dut` desde Python.
- `02_stimuli_p1`: estímulos simples.
- `03_stimuli_p2`: estímulos adicionales y espera de tiempo.

## Section 03

- `01_fixed_sim`: simulación de duración fija.
- `02_accessing_internal_signalds_DUT`: acceso a señales internas.
- `03_reset_based_on_edge_of_other_signal`: reset sincronizado con flancos.
- `04_clock_cycles_function`: uso de `ClockCycles`.

## Section 04

- `01_custom_clock`: clocks generados manualmente.
- `02_built_in_clock`: helper `Clock` de cocotb.
- `03_sync_and_async_func`: funciones síncronas y asíncronas.

## Section 05

- `01_radix_operation`: representación y radix.
- `02_priority_encoder`: verificación de priority encoder.
- `03_integer`: conversiones a enteros.

## Section 06

- `01_understanding_fork`: introducción a tareas concurrentes.
- `02_operation_fork`: uso de `cocotb.fork`.
- `03_operation_start_soon`: uso de `start_soon`.
- `04_operation_await_start`: uso de `await cocotb.start`.
- `05_used_cases`: caso de uso con clock y reset concurrentes.

## Section 07

- `01_4-bit-adder`: sumador de 4 bits.
- `02_8_mux`: mux de 8 entradas de 1 bit.
- `03_8-bits_mux`: mux de entradas de 8 bits.
- `04_4-bit_ripple_carry_adder`: ripple carry adder de 4 bits.

## Section 08

- `01_D_flip_flop`: flip-flop D con clock/reset.
- `02_memory`: memoria con escrituras y lecturas.
