# -*- coding: utf-8 -*-

import sys
import re


def parse_mecab(s):
    u""" 

    MeCab format:
    表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    """

    d = {"surface":"dummy", "pos":"dummy", "pos1":"dummy", "pos2":"dummy",
         "pos3":"dummy", "katsu":"dummy", "katsu1":"dummy", "base":"dummy",
         "yomi":"dummy", "pron":"dummy", "ex":"dummy"}

    match = re.search(r"(.*?)\t(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?$)", s)
    if match:
        d["surface"] = match.group(1)
        d["pos"] = match.group(2)
        d["pos1"] = match.group(3)
        d["pos2"] = match.group(4)
        d["pos3"] = match.group(5)
        d["katsu"] = match.group(6)
        d["katsu1"] = match.group(7)
        d["base"] = match.group(8)
        d["yomi"] = match.group(9)
        d["pron"] = match.group(10)
        d["ex"] = ""
    # else:
    #     d["ex"] = s

    return d

def parse_neko():
    nekolist = list()
    with open("../data/neko.txt.mecab", "r", encoding="utf8") as f:
        for line in f:
            parsed = parse_mecab(line)
            if parsed:
                nekolist.append(parsed)

    return nekolist

def main():
    print(parse_neko())
    print(len(parse_neko()))

if __name__ == '__main__':
    main()
