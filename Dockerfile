# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app


CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "postputprinter:app", "-b", "0.0.0.0:8051"]

