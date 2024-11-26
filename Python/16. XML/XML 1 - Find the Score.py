# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    #attr = 0
    #for child in node.iter():
    #    if child.attrib:
    #        attr += len(child.attrib)
    #return attr
    return sum(len(elem.items()) for elem in node.iter())


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))