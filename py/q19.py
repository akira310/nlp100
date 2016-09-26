# -*- coding: utf-8 -*-
import collections

with open("../data/hightemp.txt", "r", encoding="utf8") as f:
    clm = list()
    while True:
        l = f.readline()
        if l:
            clm.append(l.split("\t")[0])
        else:
            break

for d in sorted(collections.Counter(clm).items(), key=lambda x: x[1], reverse=True):
    print(d[0])
