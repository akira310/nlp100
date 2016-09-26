# -*- coding: utf-8 -*-

import gzip
import json


with gzip.open("../data/jawiki-country.json.gz", "rt", encoding="utf8") as f:
    while True:
        l = f.readline()
        if l:
            if json.loads(l, encoding="utf-8")["title"] == u"イギリス":
                s = json.loads(l, encoding="utf-8")["text"]
                print(s)
        else:
            break

