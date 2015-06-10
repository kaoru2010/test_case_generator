#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from event_sequence_list_testing.test_generator import event_sequence_test
from example import ExampleDataSource

@event_sequence_test(ExampleDataSource())
class TestExample(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def onStart(self):
        pass

    def onResume(self):
        pass

    def onPause(self):
        pass

    def onStop(self):
        pass

    def onDestroy(self):
        pass

    def surfaceCreated(self):
        pass

    def surfaceChanged(self):
        pass

    def surfaceDestroyed(self):
        pass

if __name__ == '__main__':
    unittest.main()
