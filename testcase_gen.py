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

        start = 0,
        max_visited_count = 2
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

        start = 0,
        max_visited_count = 2
    )

labels = [
    'surfaceCreated',
    'surfaceChanged',
    'surfaceDestroyed',
]

#for result in sequential([['onCreate']], merge_list(state_map1.gen_all_list(), state_map2.gen_all_list())):
#    print result

def print_java(package, className, labels, data):
    label_to_index = {}
    i = 0
    for label in labels:
        label_to_index[label] = i
        i += 1

    print "package %s;" % package
    print
    print "public class " + className + " implements DataProvider {"
    print
    print "    public interface TestCase {"
    for label in labels:
        print "        void " + label + "();"
    print "    }"
    print
    print "    private static final int[][] DATA = {"
    for row in data:
        print "            {" + (", ".join([("%d" % label_to_index[x]) for x in row])) + "},"
    print "    };"
    print
    print "    private static final String[] LABELS = {"
    for label in labels:
        print '            "' + label + '",'
    print "    };"
    print
    print "    @Override"
    print "    public int[][] getData() {"
    print "        return DATA;"
    print "    }"
    print
    print "    @Override"
    print "    public String[] getLabels() {"
    print "        return LABELS;"
    print "    }"
    print
    print "    @Override"
    print "    public String getName(int index) {"
    print "        StringBuilder sb = new StringBuilder();"
    print "        for (int event : getData()[index]) {"
    print "            sb.append(getLabels()[event]);"
    print '            sb.append(" ");'
    print "        }"
    print
    print "        return sb.toString().trim();"
    print "    }"
    print "}"


print_java(
    'com.example.kaoru.eventsequencelisttestrunner',
    'ExampleDataSource',
    labels,
    state_map2.gen_all_list())
