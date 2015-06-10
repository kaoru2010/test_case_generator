#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_python(out, package, import_list, class_name, labels, data):
    label_to_index = {}
    i = 0
    for label in labels:
        label_to_index[label] = i
        print "%4d %s" % (i, label)
        i += 1

    print >>out, '#!/usr/bin/env python'
    print >>out, '# -*- coding: utf-8 -*-'
    print >>out, '#'
    print >>out, '# このファイルは自動生成されているので直接編集しないでください。'
    print >>out, '#'
    print >>out
    print >>out, "# package %s;" % package

    for entry in import_list:
        print >>out, "import %s" % entry

    print >>out
    print >>out, "class " + class_name + ":"
    print >>out
    print >>out, "    DATA = ["

    for row in data:
        print >>out, "            [" + (", ".join([("%d" % label_to_index[x]) for x in row])) + "],"

    print >>out, "    ]"
    print >>out
    print >>out, "    LABELS = ["

    for label in labels:
        print >>out, '            "' + label + '",'

    print >>out, "    ]"
    print >>out
    print >>out, "    def getData(self):"
    print >>out, "        return self.DATA"
    print >>out
    print >>out, "    def getLabels(self):"
    print >>out, "        return self.LABELS"
    print >>out
    print >>out, "    def getName(self, index):"
    print >>out, "        return ' '.join([self.LABELS[x] for x in self.DATA[i]])"
