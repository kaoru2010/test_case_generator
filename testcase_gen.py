#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

class StateMap:
    def __init__(self, state_list, transition_table, start):
        self.state_list = state_list;
        self.transition_table = transition_table;
        self.start = start

    def gen_all_list(self, max_visited_count = 1):
        all_list = []
        self._walk(all_list, self.start, max_visited_count)
        return all_list

    def _walk(self, all_list, state, max_visited_count, state_list = None):
        if state_list is None:
            state_list = []

        state_list.append(state)

        if len(self.transition_table[state]) == 0:
            all_list.append([self.state_list[x] for x in state_list])
            return

        for dst in self.transition_table[state]:
            if state_list.count(dst) < max_visited_count:
                self._walk(all_list, dst, max_visited_count, list(state_list))

def gen_merged(list1, list2, combination):
    index1 = 0
    index2 = 0
    for x in range(0, len(list1) + len(list2)):
        if x in combination:
            yield list1[index1]
            index1 += 1
        else:
            yield list2[index2]
            index2 += 1

def gen_combination(list1, list2):
    for combination in itertools.combinations(range(0, len(list1) + len(list2)), len(list1)):
        yield [x for x in gen_merged(list1, list2, combination)]

def merge_list(*list_of_state_list):
    if len(list_of_state_list) <= 1:
        return list_of_state_list[0]

    result = []
    for list1 in list_of_state_list[0]:
        for list2 in list_of_state_list[1]:
            result.extend([x for x in gen_combination(list1, list2)])

    return merge_list(result, *list_of_state_list[2:])

def sequential(*list_of_state_list):
    if len(list_of_state_list) <= 1:
        return list_of_state_list[0]

    result = []
    for list1 in list_of_state_list[0]:
        for list2 in list_of_state_list[1]:
            result.append(list1 + list2)

    return sequential(result, *list_of_state_list[2:])


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

#for result1 in state_map1.gen_all_list(limit):
#    for result2 in state_map2.gen_all_list(limit):
#        gen_combination(result1, result2)

