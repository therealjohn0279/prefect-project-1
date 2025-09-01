#!/bin/bash

set -e

echo "Running post-create setup..."

# Let uv handle the virtual environment automatically
uv sync
uv add ruff

# Prefect setup
echo "Initializing Prefect..."
uv run prefect config set PREFECT_UI_URL="http://localhost:4200"
uv run prefect config set PREFECT_API_URL="http://localhost:4200/api"
echo "Starting Prefect server..."
nohup uv run prefect server start --host 0.0.0.0 --port 4200 > /tmp/prefect.log 2>&1 &

sleep 3

echo "Post-create setup complete!"
echo "Python version: $(uv run python --version)"
echo "uv version: $(uv --version)"