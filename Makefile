ci-local:
	uv sync --extra dev
	uv run pre-commit run --all-files
	uv run pytest --cov=prefect_project_1 --cov-report=xml --cov-fail-under=95
