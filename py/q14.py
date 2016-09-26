# -*- coding: utf-8 -*-
import argparse
import linecache

p = argparse.ArgumentParser(description="q14")
p.add_argument("N", metavar="N", type=int,   nargs=1, help="num")
args = p.parse_args()

if 0 < args.N[0]:
    with open("../data/hightemp.txt", "r", encoding="utf8") as f:
        for i in range(args.N[0]):
            l = f.readline()
            if not l:
                break
            print(l)
