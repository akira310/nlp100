# -*- coding: utf-8 -*-

def cipher(s):
    encr = ""
    print(s)
    for c in s:
        c = chr(219 - ord(c)) if c.islower() else c
        encr += c

    return encr

print(cipher(cipher("teSt")))
print(cipher(cipher("1e T")))

