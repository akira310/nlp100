# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", "r", encoding="utf8") as fr:
    with open("../data/hightemp_sp.txt", "w") as fw:
        fw.write(fr.read().replace("\t", " "))
