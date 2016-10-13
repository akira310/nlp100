# -*- coding: utf-8 -*-

import re


with open("../data/jawiki-country.json.uk", "r", encoding="utf8") as f:
    line = f.readlines()

ptrn = r"(^=+)(.*?)(=+$)"

for l in line:
    match = re.search(ptrn, l)
    if match:
        len_h = len(match.group(1)) - 1
        len_f = len(match.group(3)) - 1
        print(match.group(1), match.group(2), match.group(3))
        print(len_h if len_h<=len_f else len_f, ":", match.group(2))
