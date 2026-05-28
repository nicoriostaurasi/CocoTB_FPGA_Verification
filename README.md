# CocoTB FPGA Verification Docker Environment

This repository contains cocotb exercises that are intended to be run from each test directory with:

```sh
make icarus=sim
```

The Docker image provides a reproducible Linux simulation environment for Windows and Linux hosts:

- Python 3.11
- cocotb 1.9.2
- Icarus Verilog
- GNU Make and build tools

The cocotb version is pinned to 1.x because some exercises use legacy APIs such as `cocotb.coroutine`, `cocotb.fork`, and `cocotb.binary.BinaryValue`.

## Prerequisites

On Windows, Docker Desktop must be installed and running before building or running the image. If this command fails:

```powershell
docker info
```

with an error similar to:

```text
failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine
```

open Docker Desktop, wait until it finishes starting, and retry the command. This means the Docker client is installed, but the Linux Docker engine is not running.

## Build

From the repository root:

```sh
docker build -t cocotb-fpga-verification:local .
```

Or with Docker Compose:

```sh
docker compose build
```

## Enter The Container

For course work, the most convenient flow is to enter the Docker container once and move between exercise folders from there.

PowerShell:

```powershell
docker compose run --rm cocotb bash
```

Inside the container, the repository is mounted at `/work`:

```sh
cd /work
cd part_02/section_01/01_generation_signals
make clean
make icarus=sim
```

Then you can move to another exercise and run the same commands:

```sh
cd /work/part_02/section_08/02_memory
make clean
make icarus=sim
```

Use `make clean` before `make icarus=sim` when changing machines, Docker images, or Icarus versions. Otherwise cocotb may reuse an old `sim_build/sim.vvp` file and fail with an error like:

```text
VVP input file 12.0 can not be run with run time version 11.0
```

## Run One Test

PowerShell:

```powershell
docker run --rm -it -v ${PWD}:/work -w /work/part_02/section_01/01_generation_signals cocotb-fpga-verification:local bash -lc "make clean && make icarus=sim"
```

Bash:

```sh
docker run --rm -it -v "$PWD":/work -w /work/part_02/section_01/01_generation_signals cocotb-fpga-verification:local bash -lc "make clean && make icarus=sim"
```

Docker Compose:

```sh
docker compose run --rm -w /work/part_02/section_01/01_generation_signals cocotb bash -lc "make clean && make icarus=sim"
```

## Run All Tests

```sh
docker run --rm -it -v "$PWD":/work cocotb-fpga-verification:local run-cocotb-tests
```

On PowerShell, use:

```powershell
docker run --rm -it -v ${PWD}:/work cocotb-fpga-verification:local run-cocotb-tests
```

You can also run a subtree:

```sh
docker run --rm -it -v "$PWD":/work cocotb-fpga-verification:local run-cocotb-tests /work/part_02/section_08
```
