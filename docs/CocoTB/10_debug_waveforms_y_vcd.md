# Debug con waveforms y VCD

Los ejercicios generan `dump.vcd`, un archivo de ondas que puede abrirse con herramientas como GTKWave.

## Generación desde HDL

En `adder.sv` aparece:

```systemverilog
initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1,top);
end
```

- `$dumpfile`: nombre del archivo de ondas.
- `$dumpvars`: jerarquía y señales a volcar.

## Para qué sirve

El VCD permite ver:

- cambios de entradas y salidas
- flancos de clock
- reset
- escrituras y lecturas de memoria
- relación entre logs y tiempo de simulación

## Flujo recomendado de debug

1. Correr el test.
2. Leer el log de cocotb.
3. Si falla, abrir `dump.vcd`.
4. Buscar el tiempo donde aparece el error.
5. Comparar señales de entrada, salida y estado interno.

## Cuidado con versionar VCD

Los VCD son artefactos generados. Pueden ser útiles para clase, pero suelen cambiar cada vez que se corre una simulación. En proyectos reales normalmente se ignoran en Git.
