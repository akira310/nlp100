# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", "r", encoding="utf8") as f:
    l = f.readline()
    lines = list()
    while l:
        lines.append(l.rstrip().split("\t"))
        l = f.readline()

for l in sorted(lines, key=lambda x:x[2]):
    print(l)

