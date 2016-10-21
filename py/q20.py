# -*- coding: utf-8 -*-

import io
import sys
import gzip
import json


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with gzip.open("../data/jawiki-country.json.gz", "rt", encoding="utf8") as f:
    for l in f:
        if json.loads(l, encoding="utf-8")["title"] == u"イギリス":
            s = json.loads(l, encoding="utf-8")["text"]
            print(s)

