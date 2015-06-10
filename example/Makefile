PROJECT_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
PYTHONPATH ?= $(realpath $(PROJECT_DIR)/..)

TESTCASES += atomic_increment_testcase.py
TESTCASES += example_testcase.py

all:
	for f in $(TESTCASES); do \
		env PYTHONPATH=$(PYTHONPATH) python $$f; \
	done
