# -*- coding: utf-8 -*-

import sys
import q30

def sort_neko():
    nekos = q30.parse_neko()
    d = dict()

    for neko in nekos:
        if neko["surface"] != "dummy":
            d[neko["surface"]] = 1 if neko["surface"] not in d else d[neko["surface"]]+1

    return sorted(d.items(), key=lambda x: x[1], reverse=True)

def main():
    print(sort_neko())


if __name__ == '__main__':
    main()
