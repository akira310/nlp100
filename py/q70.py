# -*- coding: utf-8 -*-
import sys
import argparse
import os
import random

def create_sentiment():
    path_base = os.path.join("..", "data", "q70", "rt-polaritydata")
    line = list()

    with open(os.path.join(path_base, "rt-polarity.pos"), "r", encoding="latin_1") as f_p,\
         open(os.path.join(path_base, "rt-polarity.neg"), "r", encoding="latin_1") as f_n:
        line += [u"+1 "+l for l in f_p]
        line += [u"-1 "+l for l in f_n]

    with open(os.path.join(path_base, "sentiment.txt"), "w", encoding="latin_1") as f:
        random.shuffle(line)
        f.writelines(line)

def main():
    p = argparse.ArgumentParser(description="q70")
    p.add_argument("-c", "--create", action="store_true", default=False,
                   help="create sentiment.txt (default: False)")
    args = p.parse_args()

    if args.create:
        create_sentiment()
    else:
        p.print_usage()

if __name__ == '__main__':
    main()
