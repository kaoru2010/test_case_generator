<?php
#
# このファイルは自動生成されているので直接編集しないでください。
#
# PHP 5.5以降で動作します。
#

# package com.example;

class ExampleDataSource implements IteratorAggregate {

    private $DATA = [
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
    ];

    private $LABELS = [
            "userA",
            "userB",
    ];

    public function getData() {
        return $this->DATA;
    }

    public function getLabels() {
        return $this->LABELS;
    }

    public function getIterator() {
        foreach($this->DATA as $row) {
            yield array_map(function($x)
            {
                return $this->LABELS[$x];
            }, $row);
        }
    }
}
