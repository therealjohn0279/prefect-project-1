#!/bin/bash

set -e

echo "Running post-create setup..."

# Check uv installation
echo "uv version: $(uv --version)"

# Create virtual environment in .venv
echo " Creating virtual environment..."
uv venv .venv --clear
uv add ruff
uv sync

# Activate virtual environment
source .venv/bin/activate

# Install project in development mode with dev dependencies
echo "Installing project dependencies..."
uv pip install -e .

# Prefect
echo "Initializing Prefect..."
prefect config set PREFECT_UI_URL="http://localhost:4200"
prefect config set PREFECT_API_URL="http://localhost:4200/api"
echo "🚀 Starting Prefect server..."
nohup prefect server start --host 0.0.0.0 --port 4200 > /tmp/prefect.log 2>&1 &

# Wait a moment for server to start
sleep 3


# Verify installations
echo "Post-create setup complete!"
echo "Python version: $(python --version)"
echo "uv version: $(uv --version)"
echo "Pytest version: $(pytest --version)"
echo "Ruff version: $(ruff --version)"