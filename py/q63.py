# -*- coding: utf-8 -*-
import sys
import gzip
import json
import redis


def createDB():
    conn = redis.Redis(host='localhost', port=6379)
    conn.flushall()

    with open("../data/artist.json", "rt", encoding="utf-8") as f:
        for line in f:
            artist =json.loads(line, encoding="utf-8")
            if "tags" in artist:
                for tag in artist["tags"]:
                    # print(artist["name"], tag)
                    conn.lpush(artist["name"], json.dumps(tag))

def main():
    conn = redis.Redis(host='localhost', port=6379)
    type = conn.type("Oasis")
    if type == b"list":
        print(conn.lrange("Oasis", 0, -1))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        createDB()
    else:
        main()
