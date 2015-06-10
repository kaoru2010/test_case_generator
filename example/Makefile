PROJECT_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
PYTHONPATH ?= $(realpath $(PROJECT_DIR)/..)
PYTHON_BIN := env PYTHONPATH=$(PYTHONPATH) python
TESTCASE_GEN := $(PROJECT_DIR)/../testcase_gen.py

TESTCASES += atomic_increment_testcase.test_log
TESTCASES += example_testcase.test_log

all: $(TESTCASES)

atomic_increment_testcase.test_log: atomic_increment_testcase.py
	$(PYTHON_BIN) atomic_increment_testcase.py

example.py: example.in
	$(TESTCASE_GEN) example.in example.py

example_testcase.test_log: example_testcase.py example.py
	$(PYTHON_BIN) example_testcase.py
