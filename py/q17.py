# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", "r", encoding="utf8") as f:
    l = f.readline()
    clm = list()
    while l:
        clm.append(l.split("\t")[0])
        l = f.readline()

print(set(clm))

