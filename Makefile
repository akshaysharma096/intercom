.PHONY: help lint security unit integration test
.DEFAULT_GOAL := help

build: ## Build docker image
	docker build --tag intercom-test-akshaysharma .

run: ## Run docker image
	docker run --rm intercom-test-akshaysharma

integration: ## Run integration tests
	tox -e integration

test: ## Run tests
	tox --parallel--
	safe-build

unit: ## Run unit tests
	tox -e unit

safety:
	tox -e safety

clean: ## Remove project artifacts
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -rf
	rm -rf .venv/ venv/ .cache/ .tox/ .pytest_cache/