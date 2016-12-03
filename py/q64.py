# -*- coding: utf-8 -*-
import sys
import argparse
import json
import pymongo


def get_collection(dbname, coname, renewdb=False):
    mc = pymongo.MongoClient(host='localhost', port=27017)
    if renewdb:
        mc.drop_database(dbname)
    db = eval("mc."+dbname)
    co = eval("db."+coname)
    return mc, db, co


def createDB():
    mc, db, co = get_collection(dbname="artist_json", coname="artist", renewdb=True)
    with open("../data/artist.json", "rt", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(i)
            co.insert_one(json.loads(line, encoding="utf-8"))

def createDB2():
    mc, db, co = get_collection(dbname="artist_json", coname="artist", renewdb=True)
    obj = list()
    with open("../data/artist.json", "rt", encoding="utf-8") as f:
        for i, line in enumerate(f):
            obj.append(json.loads(line, encoding="utf-8"))
            if len(obj) >= 1000:
                print(i)
                co.insert_many(obj)
                obj.clear()
        print(i)
        co.insert_many(obj)

def createIndex():
    mc, db, co = get_collection(dbname="artist_json", coname="artist")
    models = list()
    indexes = [("name", pymongo.ASCENDING),
               ("aliases.name", pymongo.ASCENDING),
               ("tags.value", pymongo.ASCENDING),
               ("rating.value", pymongo.ASCENDING)]
    for index in indexes:
        models.append(pymongo.IndexModel([index]))
    co.create_indexes(models)

def main():
    p = argparse.ArgumentParser(description="q64")
    p.add_argument("create", metavar="create", type=str,   nargs=1, help="db | index")
    args = p.parse_args()

    if args.create[0] == "db":
        # createDB()
        createDB2()
    elif args.create[0] == "index":
        createIndex()
    else:
        print(args.create[0], "is undefined")

if __name__ == '__main__':
    main()
