.PHONY: help lint security unit integration test
.DEFAULT_GOAL := help

build: ## Build docker image
	docker build --tag intercom-test-akshaysharma .

run: ## Run docker image
	docker run --rm intercom-test-akshaysharma

integration: ## Integration tests
	tox -e integration

test: ## Run full-test suite
	tox --parallel--
	safe-build

unit: ## Unit tests
	tox -e unit

safety: ## Run safety checks.
	tox -e safety

clean: ## Remove temp files
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -rf
	rm -rf .venv/ venv/ .cache/ .tox/ .pytest_cache/