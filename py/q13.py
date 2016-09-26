# -*- coding: utf-8 -*-

with open("../data/col12.txt", "w", encoding="utf8") as f:
    with open("../data/col1.txt", "r") as f1:
        with open("../data/col2.txt", "r") as f2:
            l1 = f1.readline()
            l2 = f2.readline()
            for i in range(len(l1)):
                f.write(l1[i]+"\t"+l2[i]+"\n")
