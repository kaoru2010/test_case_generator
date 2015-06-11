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


class Process(object):
    def __init__(self, context):
        self.context = context
        self.terminated = False
        self.crashed = False
        self.logic = self._logic()

    def run(self):
        if self.terminated:
            return

        try:
            self.logic.next()
        except StopIteration:
            self.terminated = True

    def crash(self):
        if self.terminated:
            return

        self.logic.close()
        self.terminated = True
        self.crashed = True


class AtomicIncrementProcess(Process):
    "最大yieldの数 + 1"
    N = 3

    def _logic(self):
        yield

        yield

        tmp = self.context.value
        tmp += 1
        self.context.value = tmp

data = SEQ(
    PARA(
        PARA([[0] * AtomicIncrementProcess.N], [[2]]),
        PARA([[1] * AtomicIncrementProcess.N], [[3]])
    )
)

@event_sequence_test_raw(labels=['userA', 'userB', 'crashA', 'crashB', 'reset'], data=data)
class TestAtomicIncrement(unittest.TestCase):
    def setUp(self):
        self.context = Context(0)
        self.connectionA = AtomicIncrementProcess(self.context)
        self.connectionB = AtomicIncrementProcess(self.context)

    def tearDown(self):
        if self.connectionA.crashed and self.connectionB.crashed:
            self.assertEqual(0, self.context.value)
        elif (not self.connectionA.crashed) and (not self.connectionB.crashed):
            self.assertEqual(2, self.context.value)
        else:
            self.assertEqual(1, self.context.value)

    def userA(self):
        self.connectionA.run()

    def crashA(self):
        self.connectionA.crash()

    def userB(self):
        self.connectionB.run()

    def crashB(self):
        self.connectionB.crash()

if __name__ == '__main__':
    unittest.main()
