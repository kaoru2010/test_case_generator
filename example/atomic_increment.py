#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# このファイルは自動生成されているので直接編集しないでください。
#

# package com.example;

class ExampleDataSource:

    DATA = [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0, 0],
    ]

    LABELS = [
            "userA",
            "userB",
    ]

    def getData(self):
        return self.DATA

    def getLabels(self):
        return self.LABELS

    def getName(self, index):
        return ' '.join([self.LABELS[x] for x in self.DATA[i]])
