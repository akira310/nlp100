# -*- coding: utf-8 -*-
import sys
import argparse
import json
import pymongo
import q64


def findDB(name="Queen", area="Japan"):
    mc, db, co = q64.get_collection(dbname="artist_json", coname="artist")
    print("name:", name)
    print(list(co.find({"name": name})))
    print("\n\n\n")

    findlist = list()
    if name:
        findlist.append({"name": name})
    if area:
        findlist.append({"area": area})

    if len(findlist) > 1:
        findand = {"$and": findlist}
    else:
        findand = findlist[0]

    # print(list(co.find({'$and': [{'name': name}, {'area': area}]})))
    print(list(co.find(findand)))

def main():
    if len(sys.argv) > 1:
        findDB(sys.argv[1])
    else:
        print("no argv")
        findDB()

if __name__ == '__main__':
    main()
