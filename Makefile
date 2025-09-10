PY := python3
PIP := pip

.PHONY: install lint test

install:
	$(PIP) install -e .[dev]
	pre-commit install

lint:
	pre-commit run --all-files

test:
	pytest -q

