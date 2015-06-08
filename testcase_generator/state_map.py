#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

class StateMap:
    def __init__(self, state_list, transition_table, start, max_visited_count = 1):
        self.state_list = state_list;
        self.transition_table = transition_table;
        self.start = start
        self.max_visited_count = max_visited_count

    def gen_all_list(self, max_visited_count = None):
        if max_visited_count is None:
            max_visited_count = self.max_visited_count

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
