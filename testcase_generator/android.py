#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_java(out, package, import_list, class_name, labels, data):
    label_to_index = {}
    i = 0
    for label in labels:
        label_to_index[label] = i
        i += 1

    print >>out, "/**"
    print >>out, " * このファイルは自動生成されているので直接編集しないでください。"
    print >>out, " */"
    print >>out, ""
    print >>out, "package %s;" % package

    for entry in import_list:
        print >>out, "import %s;" % entry

    print >>out
    print >>out, "public class " + class_name + " implements DataProvider {"
    print >>out, ''
    print >>out, "    public interface TestCase {"

    for label in labels:
        print >>out, "        void " + label + "();"

    print >>out, "    }"
    print >>out
    print >>out, "    private static final int[][] DATA = {"

    for row in data:
        print >>out, "            {" + (", ".join([("%d" % label_to_index[x]) for x in row])) + "},"

    print >>out, "    };"
    print >>out
    print >>out, "    private static final String[] LABELS = {"

    for label in labels:
        print >>out, '            "' + label + '",'

    print >>out, "    };"
    print >>out, ""
    print >>out, "    @Override"
    print >>out, "    public int[][] getData() {"
    print >>out, "        return DATA;"
    print >>out, "    }"
    print >>out, ""
    print >>out, "    @Override"
    print >>out, "    public String[] getLabels() {"
    print >>out, "        return LABELS;"
    print >>out, "    }"
    print >>out
    print >>out, "    @Override"
    print >>out, "    public String getName(int index) {"
    print >>out, "        StringBuilder sb = new StringBuilder();"
    print >>out, "        for (int event : getData()[index]) {"
    print >>out, "            sb.append(getLabels()[event]);"
    print >>out, '            sb.append(" ");'
    print >>out, "        }"
    print >>out
    print >>out, "        return sb.toString().trim();"
    print >>out, "    }"
    print >>out, "}"
