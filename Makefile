.DEFAULT_GOAL:=help

.PHONY: dev
dev: ## Installs adapter in develop mode
	@\
	pip install -e . -r dev-requirements.txt

.PHONY: dev-uninstall
dev-uninstall: ## Uninstalls all packages while maintaining the virtual environment
	pip freeze | grep -v "^-e" | cut -d "@" -f1 | xargs pip uninstall -y
	pip uninstall -y dbt-incident
