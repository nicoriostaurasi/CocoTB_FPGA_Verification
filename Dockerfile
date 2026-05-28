FROM python:3.11-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        build-essential \
        ca-certificates \
        git \
        iverilog \
        make \
        tcl \
        time \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY scripts/run-cocotb-tests.sh /usr/local/bin/run-cocotb-tests
RUN chmod +x /usr/local/bin/run-cocotb-tests

CMD ["bash"]
