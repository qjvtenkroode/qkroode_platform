.PHONY: clean clean-pyc
VENV=~/playground//virtualenvs/qkroode_platform

help:
	@echo "\t"
	@echo "Help me!"
	@echo "\t bootstrap - create a virtualenv and install the required packages."
	@echo "\t bootstrap-dev - create a virtualenv and install the required packages for development."
	@echo "\t clean - cleans everything, using clean-pyc"
	@echo "\t clean-pyc - remove python artifacts"
	@echo "\t test - run all tests"
	@echo "\t test-pylint - run pylint tests"
	@echo "\t test-pytest - run pytest tests"
	@echo "\t"

$(VENV)/bin/pip:
	virtualenv $(VENV)

bootstrap: $(VENV)/bin/pip
	$(VENV)/bin/pip install -r requirements.txt

bootstrap-dev: $(VENV)/bin/pip
	$(VENV)/bin/pip install -r dev_requirements.txt

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

test: test-pytest test-pylint

test-pylint:
	@echo "Running pylint:\n"
	$(VENV)/bin/pylint --ignore='E501' ./qkroode_platform
	@echo "\n"

test-pytest:
	@echo "Running pytest:\n"
	PYTHONPATH=./qkroode_platform $(VENV)/bin/py.test --cov=qkroode_platform --cov-report term-missing
	@echo "\n"
