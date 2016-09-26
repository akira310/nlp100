# -*- coding: utf-8 -*-
import argparse
import linecache

p = argparse.ArgumentParser(description="q14")
p.add_argument("N", metavar="N", type=int,   nargs=1, help="num")
args = p.parse_args()

with open("../data/hightemp.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

if 0 < args.N[0]:
    for i, l in enumerate(lines[-args.N[0]:]):
        print(i+1,l)
