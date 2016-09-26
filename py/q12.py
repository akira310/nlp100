# -*- coding: utf-8 -*-

with open("../data/hightemp.txt", "r", encoding="utf8") as f:
    with open("../data/col1.txt", "w") as f1:
        with open("../data/col2.txt", "w") as f2:
            for l in f.readlines():
                f1.write(l[0])
                f2.write(l[1])
