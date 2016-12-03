# -*- coding: utf-8 -*-
import sys
import redis


def main():
    conn = redis.Redis(host='localhost', port=6379)
    cnt = 0
    for name in  conn.keys():
        if conn.get(name) == b"Japan":
            # print(name)
            cnt += 1
    print(cnt)

def test():
    conn = redis.Redis(host='localhost', port=6379)
    for key in conn.keys("Oasis"):
        if key.decode("utf-8") == "Oasis":
            print("match")
        print(key)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
