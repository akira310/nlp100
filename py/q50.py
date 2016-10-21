# -*- coding: utf-8 -*-

import sys
import re

def parse(l, s):
    remain = s
    match = re.search(u"(.*?)[\.|;|:|?|!]\s+([A-Z0-9].*$)", remain, re.DOTALL)
    if match:
        l.append(match.group(1))
        remain = parse(l, match.group(2))
    return remain

def main():
    with open("../data/nlp.txt", "r") as f:
        s = ""
        sentence = list()
        for line in f:
            s = parse(sentence, s+line)
        sentence.append(s)

        for l in sentence:
            print(l.replace("\n", " ").replace("\r", " "))

def test():
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
