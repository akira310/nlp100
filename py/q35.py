# -*- coding: utf-8 -*-

import sys
import re
import q30


def main():
    nekos = q30.parse_neko()
    find = list()
    for neko in nekos:
        if neko["pos"] == u"名詞":
            find.append(neko["surface"])
        else:
            if len(find) >= 2:
                print(find)
            find.clear()

if __name__ == '__main__':
    main()
