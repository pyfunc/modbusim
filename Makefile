.PHONY: install test lint format clean

# Variables
PYTHON = python
PIP = pip
POETRY = poetry

# Install dependencies
install:
	$(POETRY) install

# Run tests
test:
	$(POETRY) run pytest -v --cov=modbusim --cov-report=term-missing

# Run linter
lint:
	$(POETRY) run flake8 modbusim tests
	$(POETRY) run mypy modbusim tests

# Format code
format:
	$(POETRY) run black modbusim tests
	$(POETRY) run isort modbusim tests

# Clean up
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	rm -rf .coverage htmlcov/ build/ dist/ *.egg-info/


# Sprawdzenie wersji
version:
	@echo "Aktualna wersja:"
	@poetry version

# Inkrementacja wersji patch
bump-patch:
	poetry version patch

# Inkrementacja wersji minor
bump-minor:
	poetry version minor

# Inkrementacja wersji major
bump-major:
	poetry version major

# Zbudowanie paczki do dystrybucji
build: clean
	poetry build

# Sprawdzenie czy wersja jest gotowa do publikacji
check-version:
	@echo "Sprawdzanie wersji..."
	@poetry version
	@echo "Upewnij się, że wersja jest unikalna przed publikacją."

# Publikacja paczki w PyPI
publish: check-version bump-patch build
	@echo "Publikowanie w PyPI..."
	poetry publish

# Publikacja paczki w TestPyPI
publish-test: check-version build
	@echo "Publikowanie w TestPyPI..."
	poetry publish --build -r testpypi
	@echo "\nPaczka opublikowana w TestPyPI. Możesz ją zainstalować używając:"
	@echo "pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple modapi"
