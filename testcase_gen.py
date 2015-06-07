#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from testcase_generator.state_map import StateMap
from testcase_generator.utils import merge_list
from testcase_generator.utils import sequential

state_map1 = StateMap(
        state_list = [
            'onStart',
            'onResume',
            'onPause',
            'onStop',
            'onDestroy',
        ],

        transition_table = [
            [1, 3],
            [2],
            [1, 3],
            [0, 4],
            [],
        ],

        start = 0
    )

state_map2  = StateMap(
        state_list = [
            'surfaceCreated',
            'surfaceChanged',
            'surfaceDestroyed',
        ],

        transition_table = [
            [1, 2],
            [1, 2],
            [],
        ],

        start = 0
    )

limit = 2
for result in sequential([['onCreate']], merge_list(state_map1.gen_all_list(limit), state_map2.gen_all_list(limit))):
    print result
