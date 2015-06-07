#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

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
