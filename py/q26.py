# -*- coding: utf-8 -*-

import sys
import re
import q25


def remove_emphasis(s):
    restr = u"(^.*?)('+)(.*?)('+)(.*$)"

    result = s
    match = re.search(restr, s)
    if match:
        result = match.group(1) + match.group(3) + remove_emphasis(match.group(5))

    return result

def main():
    for k, v in q25.extract("国").items():
        v = remove_emphasis(v)
        try:
            print(k, v)
        except Exception as e:
            print(e)

def test():
    s = "|確立形態4 = 現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更"
    print(remove_emphasis(s))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()



