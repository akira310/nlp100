# -*- coding: utf-8 -*-
import sys
import gzip
import json
import redis


def main():
    with gzip.open("../data/artist.json.gz", "rt", encoding="utf-8") as f:
        for line in f:
            print(json.loads(line, encoding="utf-8")["name"])
            break

def test():
    conn = redis.Redis(host='localhost', port=6379)
    conn.flushall()
    conn.set("testkey", "hoge")
    print(conn.get("testkey"))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
