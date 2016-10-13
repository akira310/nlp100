# -*- coding: utf-8 -*-

import sys
import re
import q30


def main():
    nekolist = q30.parse_neko()
    for neko in nekolist:
        if neko["pos"] == u"動詞":
            print(neko["base"])

def test():
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
