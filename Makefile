SHELL := /bin/bash
USE_CONDA ?= 1  # Choose between conda and venv if necessary
INSTALL_SCRIPT = install_with_conda.sh
ifeq (false,$(USE_CONDA))
	INSTALL_SCRIPT = install_with_venv.sh
endif

.DEFAULT_GOAL = help

# help: help					- Display this makefile's help information
.PHONY: help
help:
	@grep "^# help\:" Makefile | grep -v grep | sed 's/\# help\: //' | sed 's/\# help\://'

# help: install					- Create a virtual environment and install dependencies
.PHONY: install
install:
	@bash bin/$(INSTALL_SCRIPT)

# help: install_precommit			- Install pre-commit hooks
.PHONY: install_precommit
install_precommit:
	@pre-commit install -t pre-commit
	@pre-commit install -t pre-push

# help: format			- format code using the precommits
.PHONY: format
format:
	@pre-commit run -a

# help: run_tests			- Run repository's tests
.PHONY: run_tests
run_tests:
	@pytest tests/
