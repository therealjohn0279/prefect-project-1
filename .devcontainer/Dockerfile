# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Install additional system dependencies if needed
RUN apt-get update && \
    apt-get install -y \
        git \
        curl \
        ca-certificates \
        && rm -rf /var/lib/apt/lists/* \
        && apt-get clean

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    cp /root/.local/bin/uv /usr/local/bin/uv && \
    chmod +x /usr/local/bin/uv

# Copy and set permissions for post-create script
COPY .devcontainer/post_create.sh /tmp/post_create.sh
RUN chmod +x /tmp/post_create.sh

# Switch to vscode user (already created in base image)
USER vscode
WORKDIR /workspace