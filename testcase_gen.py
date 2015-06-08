#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from optparse import OptionParser

from testcase_generator.android import print_java

#for result in sequential([['onCreate']], merge_list(state_map1.gen_all_list(), state_map2.gen_all_list())):
#    print result



parser = OptionParser()
parser.add_option("-p", "--package", dest="package", help="Package name for Java", default="com.example")
parser.add_option("-c", "--class", dest="class_name", help="Class name for Java", default="ExampleDataSource")
(options, args) = parser.parse_args()

if len(args) != 2:
    print "Usage: testcase_gen.py <INPUT> <OUTPUT>"
    quit()

if args[0] == args[1]:
    print "Error: input and output are same."
    quit()

TESTCASE_DEF = {
    'package': 'com.example',
    'import_list': [],
    'class_name': 'ExampleDataSource',
    'labels': [],
    'data': [],
}

execfile(args[0], {}, { 'TESTCASE_DEF':TESTCASE_DEF })

if options.package:
    TESTCASE_DEF['package'] = options.package

if options.class_name:
    TESTCASE_DEF['class_name'] = options.class_name

with open(args[1], 'w') as out:
    print_java(
        out,
        TESTCASE_DEF['package'],
        TESTCASE_DEF['import_list'],
        TESTCASE_DEF['class_name'],
        TESTCASE_DEF['labels'],
        TESTCASE_DEF['data'])
