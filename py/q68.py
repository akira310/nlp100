# -*- coding: utf-8 -*-
import sys
import io
import argparse
import json
import pymongo
import q64


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def sort():
    mc, db, co = q64.get_collection(dbname="artist_json", coname="artist")
    for artist in co.find({"tags.value": "dance"}).sort("rating.count", pymongo.DESCENDING).limit(10):
        print(artist["name"], ":", artist["rating"]["count"])

def main():
    sort()

if __name__ == '__main__':
    main()
