# -*- coding: utf-8 -*-
import argparse
import linecache
import glob
import os

p = argparse.ArgumentParser(description="q14")
p.add_argument("N", metavar="N", type=int,   nargs=1, help="num")
args = p.parse_args()

with open("../data/hightemp.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

if 0 < args.N[0]:
    for path in glob.glob("../data/temp_split*.txt"):
        print(path)
        os.remove(path)

    for i, p in enumerate(range(0, len(lines), args.N[0])):
        with open("../data/temp_split{}.txt".format(i), "w", encoding="utf8") as f:
            f.write("{}".format(lines[p:p+args.N[0]]))

