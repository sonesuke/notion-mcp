test: 
    uv run pytest --cov=src

check: 
    pre-commit run -a

run:
    uv sync
    uv run cli