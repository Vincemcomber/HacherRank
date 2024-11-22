# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for _ in range(int(input()))]))
parser.close()