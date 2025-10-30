ARG UV_VERSION=latest
ARG BASE_IMAGE=ubuntu


FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv


# https://hub.docker.com/r/microsoft/devcontainers-base
FROM mcr.microsoft.com/vscode/devcontainers/base:$BASE_IMAGE

ENV PYTHONDONTWRITEBYTECODE=True \
    PYTHONUNBUFFERED=True \
    UV_LINK_MODE=copy

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        just ack jq wget curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=uv --chown=vscode: /uv /uvx /bin/
