# -*- coding: utf-8 -*-

import sys
import re
import subprocess
from nltk import stem


def main():
    p = subprocess.run("python q51.py", stdout=subprocess.PIPE)
    stemmer = stem.PorterStemmer()
    for l in p.stdout.decode('utf-8').splitlines():
        print("{}\t{}".format(l, stemmer.stem(l)))

def test():
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
