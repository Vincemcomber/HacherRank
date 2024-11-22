# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

# Language: Python

# ========================
#         Solution
# ========================

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for attr in attrs:
            print ("-> {} > {}".format(*attr))

    def handle_endtag(self, tag):
        print ("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for attr in attrs:
            print ("-> {} > {}".format(*attr))

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for _ in range(int(input()))]))