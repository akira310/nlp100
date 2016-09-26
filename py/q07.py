# -*- coding: utf-8 -*-
import argparse

p = argparse.ArgumentParser(description="q07")
p.add_argument("x", metavar="x", type=int,   nargs=1, help="x value")
p.add_argument("y", metavar="y", type=str,   nargs=1, help="y value")
p.add_argument("z", metavar="z", type=float, nargs=1, help="z value")

args = p.parse_args(["12", u"気温", "22.4"])
# print(args)
print(u"{0}時の{1}は{2}".format(args.x, args.y, args.z))
