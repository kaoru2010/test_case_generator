#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from event_sequence_list_testing.test_generator import event_sequence_test_raw

from testcase_generator.state_map import StateMap
from testcase_generator.utils import ignore_StopIteration
from testcase_generator.utils import sequential_combinations as SEQ
from testcase_generator.utils import parallel_combinations as PARA

class Context:
    def __init__(self, value):
        self.value = value

def logic(context):
    tmp = context.value
    yield

    tmp += 1
    yield

    context.value = tmp

N = 3

@event_sequence_test_raw(labels=['userA', 'userB'], data=PARA([[0] * N], [[1] * N]))
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
