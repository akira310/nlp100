# -*- coding: utf-8 -*-

import re


with open("../data/jawiki-country.json.uk", "r", encoding="utf8") as f:
    line = f.readlines()

ptrn_base=u"(\s*ファイル|file\s*):\s*(.*?)"
noread = len(line)
find = 0
while noread > 0:
    match = re.search(re.compile(u"(\[\[){0}(\]\])".format(ptrn_base), re.IGNORECASE), line[-noread])
    if match:
        find+=1
        print(find, ":", match.group(3).split('|')[0])
    elif re.search(r"^\<gallery[\>| .+\>]", line[-noread]):
        noread -= 1
        while not re.search(r"^\<\/gallery[\>| .+\>]", line[-noread]):
            match = re.search(re.compile(u"{0}$".format(ptrn_base), re.IGNORECASE), line[-noread])
            if match:
                find+=1
                print(find, ":", match.group(2).split('|')[0])
            noread -= 1
    noread -= 1
