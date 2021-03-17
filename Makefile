.PHONY: help lint security unit integration test
.DEFAULT_GOAL := help

build: ## Build docker image
	docker build --tag intercom .

run: ## Run docker image
	docker run --rm intercom

integration: ## Run integration tests
	tox -e integration

test: ## Run tests
	tox --parallel--safe-build

unit: ## Run unit tests
	tox -e unit

clean: ## Remove project artifacts
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -rf
	rm -rf .venv/ venv/ .cache/ .tox/ .mypy_cache/ .pytest_cache/ .hypothesis/