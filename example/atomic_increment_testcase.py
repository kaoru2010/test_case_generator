#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from event_sequence_list_testing.test_generator import event_sequence_test
from atomic_increment import ExampleDataSource

class Context:
    def __init__(self, value):
        self.value = value

def logic(context):
    tmp = context.value
    yield

    tmp += 1
    yield

    context.value = tmp

def ignore_StopIteration(f):
    def _(self):
        try:
            f(self)
        except StopIteration:
            pass
    return _

@event_sequence_test(ExampleDataSource())
class TestAtomicIncrement(unittest.TestCase):
    def setUp(self):
        self.context = Context(0)
        self.connectionA = logic(self.context)
        self.connectionB = logic(self.context)

    def tearDown(self):
        self.assertEqual(2, self.context.value)

    @ignore_StopIteration
    def userA(self):
        self.connectionA.next()

    @ignore_StopIteration
    def userB(self):
        self.connectionB.next()

if __name__ == '__main__':
    unittest.main()
