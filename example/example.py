#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# このファイルは自動生成されているので直接編集しないでください。
#

# package com.example;

class ExampleDataSource:

    DATA = [
            [0, 1, 2, 1, 2, 3, 0, 3, 4],
            [0, 1, 2, 1, 2, 3, 4],
            [0, 1, 2, 3, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 0, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 3, 0, 1, 2, 1, 2, 3, 4],
            [0, 3, 0, 1, 2, 3, 4],
            [0, 3, 0, 3, 4],
            [0, 3, 4],
    ]

    LABELS = [
            "onStart",
            "onResume",
            "onPause",
            "onStop",
            "onDestroy",
            "surfaceCreated",
            "surfaceChanged",
            "surfaceDestroyed",
    ]

    def getData(self):
        return self.DATA

    def getLabels(self):
        return self.LABELS

    def getName(self, index):
        return ' '.join([self.LABELS[x] for x in self.DATA[i]])
