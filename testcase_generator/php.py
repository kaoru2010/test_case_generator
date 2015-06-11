# -*- coding: utf-8 -*-

def print_php(out, package, import_list, class_name, labels, data):
    label_to_index = {}
    i = 0
    for label in labels:
        label_to_index[label] = i
        print "%4d %s" % (i, label)
        i += 1

    print >>out, '<' + '?php'
    print >>out, '#'
    print >>out, '# このファイルは自動生成されているので直接編集しないでください。'
    print >>out, '#'
    print >>out, '# PHP 5.5以降で動作します。'
    print >>out, '#'
    print >>out
    print >>out, "# package %s;" % package

    for entry in import_list:
        print >>out, "import %s" % entry

    print >>out
    print >>out, "class " + class_name + " implements IteratorAggregate {"
    print >>out
    print >>out, "    private $DATA = ["

    for row in data:
        print >>out, "            [" + (", ".join([("%d" % label_to_index[x]) for x in row])) + "],"

    print >>out, "    ];"
    print >>out
    print >>out, "    private $LABELS = ["

    for label in labels:
        print >>out, '            "' + label + '",'

    print >>out, "    ];"
    print >>out
    print >>out, "    public function getData() {"
    print >>out, "        return $this->DATA;"
    print >>out, "    }"
    print >>out
    print >>out, "    public function getLabels() {"
    print >>out, "        return $this->LABELS;"
    print >>out, "    }"
    print >>out
    print >>out, "    public function getIterator() {"
    print >>out, "        foreach($this->DATA as $row) {"
    print >>out, "            yield array_map(function($x)"
    print >>out, "            {"
    print >>out, "                return $this->LABELS[$x];"
    print >>out, "            }, $row);"
    print >>out, "        }"
    print >>out, "    }"
    print >>out, "}"
