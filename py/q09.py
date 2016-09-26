# -*- coding: utf-8 -*-
import random

def typoglycemia(s):
    after = list()
    for w in s.split(" "):
        if len(w) > 4:
            l = list(w[1:-1])
            random.shuffle(l)
            w = w[0] + "".join(l) + w[-1]
        after.append(w)

    return(" ".join(after))

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(s)
print(typoglycemia(s))
