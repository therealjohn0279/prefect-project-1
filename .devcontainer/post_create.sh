#!/bin/bash

set -e

echo "Running post-create setup..."

# Check uv installation
echo "uv version: $(uv --version)"

# Install project dependencies and dev tools
echo "Installing project dependencies..."
uv sync --extra dev

# Install project in development mode
echo "Installing project in development mode..."
uv pip install -e .

# Setup pre-commit hooks
echo "Setting up pre-commit hooks..."
uv run pre-commit install

# Prefect setup
echo "Initializing Prefect..."
uv run prefect config set PREFECT_UI_URL="http://localhost:4200"
uv run prefect config set PREFECT_API_URL="http://localhost:4200/api"
echo "Starting Prefect server..."
nohup uv run prefect server start --host 0.0.0.0 --port 4200 > /tmp/prefect.log 2>&1 &

# Wait a moment for server to start
sleep 3

# Verify installations
echo "Post-create setup complete!"
echo "Python version: $(uv run python --version)"
echo "uv version: $(uv --version)"
echo "Pytest version: $(uv run pytest --version)"
echo "Ruff version: $(uv run ruff --version)"
echo "Pre-commit installed: $(uv run pre-commit --version)"