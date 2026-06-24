.PHONY: help install test lint format clean pre-commit-install

# Default target
help:
	@echo "Heiman Home - Available commands:"
	@echo ""
	@echo "  make install          Install dependencies"
	@echo "  make test             Run tests"
	@echo "  make test-cov         Run tests with coverage"
	@echo "  make lint             Run linters"
	@echo "  make format           Format code"
	@echo "  make clean            Clean up generated files"
	@echo "  make pre-commit-install  Install pre-commit hooks"
	@echo "  make release          Create a new release"
	@echo ""

# Install dependencies
install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .

# Run tests
test:
	pytest tests/ -v

# Run tests with coverage
test-cov:
	pytest tests/ --cov=custom_components/heiman_home --cov-report=html --cov-report=term-missing -v
	@echo ""
	@echo "Coverage report generated in htmlcov/"
	@echo "Open htmlcov/index.html in your browser to view the report"

# Run linters
lint:
	ruff check custom_components/heiman_home/
	mypy custom_components/heiman_home/ --ignore-missing-imports
	pylint custom_components/heiman_home/ --disable=C0114,C0115,C0116,W0613,R0913,R0902,R0914,R0915,W0718,W0719,W1514

# Format code
format:
	ruff check custom_components/heiman_home/ --fix
	ruff format custom_components/heiman_home/

# Clean up generated files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .pytest_cache/ .mypy_cache/ htmlcov/ coverage.xml .coverage
	@echo "Cleaned up generated files"

# Install pre-commit hooks
pre-commit-install:
	pre-commit install
	@echo "Pre-commit hooks installed"

# Create a new release (usage: make release version=1.0.0)
release:
ifndef version
	$(error version is required, usage: make release version=1.0.0)
endif
	@echo "Creating release v$(version)"
	@echo "Updating manifest.json..."
	python3 -c "import json; data=json.load(open('custom_components/heiman_home/manifest.json')); data['version']='$(version)'; json.dump(data, open('custom_components/heiman_home/manifest.json', 'w'), indent=2)"
	@echo "Committing changes..."
	git add custom_components/heiman_home/manifest.json
	git commit -m "chore: bump version to $(version)"
	@echo "Creating tag..."
	git tag v$(version)
	@echo "Pushing to remote..."
	git push origin main
	git push origin v$(version)
	@echo "Release v$(version) created successfully!"
	@echo "GitHub Actions will automatically create a GitHub release"
