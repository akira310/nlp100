# -*- coding: utf-8 -*-

import sys
import re


def extract(name):
    d = dict()
    with open("../data/jawiki-country.json.uk", "r", encoding="utf8") as f:
        search = True
        lastkey = ""
        for line in f:
            if search:
                if re.search(u"^{{{{基礎情報 {}".format(name), line):
                    search = False
            else: 
                match = re.search(u"\|(.+?)\s*?=\s*(.+?$)", line)
                if match:
                    d[match.group(1)] = match.group(2)
                    lastkey = match.group(1)
                elif re.search(u"^}}$", line):
                    break
                else:
                    d[lastkey] += line

    return d

def main():
    for k, v in extract("国").items():
        try:
            print(k,v)
        except Exception as e:
            print(e)

def test():
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
