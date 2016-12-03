# -*- coding: utf-8 -*-
import sys
import redis


def main():
    conn = redis.Redis(host='localhost', port=6379)
    print(conn.get("Oasis"))

def test():
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
