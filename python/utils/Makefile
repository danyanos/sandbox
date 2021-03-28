# This is a barebones Makefile to help run tests, run linting, and run the application

SHELL := /bin/bash

.DEFAULT: help

help:
	@echo "make test"
	@echo "	run tests"
	@echo "make lint"
	@echo "	run mypy and flake8"
	@echo "make run"
	@echo "	run project"

setup:
	pipenv install --dev

lint:
	pipenv run python3 -m mypy utils/string/ tests/string/ --ignore-missing-imports
	pipenv run python3 -m flake8

test: lint
	pipenv run python3 -m pytest

run: 
	pipenv run python3 app/app.py
