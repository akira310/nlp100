# -*- coding: utf-8 -*-

import sys
import re
import subprocess


def parse_word(line):
    for w in line.split():
        print(w)
    print("")   # end of line

def main():
    p = subprocess.run("python q50.py", stdout=subprocess.PIPE)
    for l in p.stdout.decode('utf-8').splitlines():
        parse_word(l)

def test():
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
