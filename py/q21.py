# -*- coding: utf-8 -*-

import io
import sys
import re


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open("../data/jawiki-country.json.uk", "r", encoding="utf8") as f:
    ptrn = r"(\[\[\s*category\s*:\s*)(.*)(\]\])"
    rptrn = re.compile(ptrn, re.IGNORECASE)
    for l in f:
        s = re.search(rptrn, l)
        if s:
            print(l)

