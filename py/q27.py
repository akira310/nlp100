# -*- coding: utf-8 -*-

import sys
import re
import q25
import q26


def remove_innerlink(s):
    restr = u"(^.*?)\[\[(.*?)\]\](.*$)"

    result = s
    match = re.search(restr, s)
    if match:
        if re.match(u"(ファイル|category):", match.group(2)):
            checkedstr = "[[" + match.group(2) + "]]"
        else:
            checkedstr = match.group(2).split("|")[-1]
        result = match.group(1) + checkedstr + remove_innerlink(match.group(3))

    return result

def main():
    for k, v in q25.extract("国").items():
        v = remove_innerlink(q26.remove_emphasis(v))
        try:
            print(k, v)
        except Exception as e:
            print(e)

def test():
    l = [
            "|元首等肩書 = [[イギリスの君主|女王]]",
            "|国章画像 = [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]"
        ]
    for s in l:
        print(remove_innerlink(s))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()



