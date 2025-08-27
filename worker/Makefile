.PHONY: help run-worker install test

help:
	@echo "Makefile options:"
	@echo "  install   Install dependencies from requirements.txt"
	@echo "  test      Test database connections"
	@echo "  start     Run worker.py with python3"
	@echo "  help      Show this help message"

install:
	pip3 install -r requirements.txt

start:
	python3 worker.py
