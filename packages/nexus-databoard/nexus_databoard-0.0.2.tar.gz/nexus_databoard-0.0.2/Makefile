.PHONY: run
run:
	@echo "Running databoard..."
	@cd ./src/nexus_databoard/ && streamlit run Home.py


.PHONY: build
build:
	@echo "Cleaning dist folder..."
	@rm -rf dist
	@echo "Building databoard..."
	@python3 -m build

.PHONY: deploy-pypi
deploy-pypi:
	@echo "Deploying nexus_databoard to PyPi..."
	@python3 -m twine upload --repository pypi dist/*