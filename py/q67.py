# -*- coding: utf-8 -*-
import sys
import argparse
import json
import pymongo
import q64


def find_aliasesname(name):
    mc, db, co = q64.get_collection(dbname="artist_json", coname="artist")
    print(list(co.find({"aliases.name": name})))

def main():
    if len(sys.argv) > 1:
        find_aliasesname(sys.argv[1])
    else:
        print("no argv")

if __name__ == '__main__':
    main()
