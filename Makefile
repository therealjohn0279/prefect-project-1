ci-local:
	uv sync --extra dev
	uv run pre-commit run --all-files
	uv run pytest --cov=python_devcontainer_template --cov-report=xml --cov-fail-under=95
