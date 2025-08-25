lint:
  - uv run -m ruff check --fix .
  - uv run -m ruff format .
test:
  - uv run pytest
typing:
  - uv run python3 -m mypy src
spacy:
  - uv run python3 -m spacy validate
all: lint typing test
