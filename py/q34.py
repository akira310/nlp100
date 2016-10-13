# -*- coding: utf-8 -*-

import sys
import re
import q30


def main():
    nekos = q30.parse_neko()
    for i, neko in enumerate(nekos):
        if neko["pos"] == u"助詞" and neko["pos1"] == u"連体化":
            print(nekos[i-1]["surface"], nekos[i]["surface"], nekos[i+1]["surface"])


if __name__ == '__main__':
    main()
