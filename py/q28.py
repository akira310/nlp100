# -*- coding: utf-8 -*-

import sys
import re
from types import *
import q25
import q26
import q27


def remove_filelink(s):
    restr = u"(^.*?)\[\[(ファイル|category):(.*?)\]\](.*$)"

    result = s
    match = re.search(restr, s)
    if match:
        result = match.group(1) + match.group(3).split("|")[-1] + remove_filelink(match.group(4))

    return result

def remove_extralink(s, i):
    restr = u"(^.*?)(\[)(https*://.+)(\])(.*$)"

    result = s
    match = re.search(restr, s)
    if match:
        # print(match.groups())
        if match.group(0) == "":
            checkedstr = match.group(3)
        else:
            if " " in match.group(3):
                checkedstr = "".join(match.group(3).split(" ")[1:])
            else:
                i = i + 1
                checkedstr = "[{}]".format(i)

        result = "{}{}{}".format(match.group(1), checkedstr,
                                 remove_extralink(match.group(5), i)[0])

    return result, i

def remove_redirect(s):
    restr = u"(^.*?)#REDIRECT \[\[(.+?)\]\](.*$)"

    result = s
    match = re.search(restr, s)
    if match:
        result = match.group(1) + match.group(2).split("|")[-1] + remove_redirect(match.group(3))

    return q27.remove_innerlink(result)

def remove_comment(s):
    restr = u"(^.*?)(<!-- )(.+?)( -->)(.*$)"

    result = s
    match = re.search(restr, s)
    if match:
        result = match.group(1) + match.group(3) + remove_comment(match.group(5))

    return result

def remove_headline(s):
    restr = u"^====*(.*?)====*$"

    result = s
    match = re.search(restr, s)
    if match:
        result = match.group(1)

    return result

def remove_bulletpoint(s):
    restr = u"^\*(\**) (.*$)"

    result = s
    match = re.search(restr, s)
    if match:
        tabs = "".join(["\t" for x in range(len(match.group(1)))]) if type(match.group(1)) is str else ""
        result = "{}{}".format(tabs, match.group(2))

    return result

def remove_markup(s, i):
    s = q26.remove_emphasis(s)
    s = remove_redirect(s)
    s = remove_filelink(s)
    s, i = remove_extralink(s, i)
    s = remove_comment(s)
    s = remove_headline(s)
    s = remove_bulletpoint(s)

    return s, i

def main():
    i = 0
    for k, v in q25.extract("国").items():
        v = remove_markup(v, i)
        try:
            print(k, v)
        except Exception as e:
            print(e)

def test():
    l = [
            "|元首等肩書 = [[イギリスの君主|女王]]",
            "|国章画像 = [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]",
            "[http://www.example.org]",
            "[http://www.example.org 表示文字]",
            "http://www.example.org",
            "[http://www.example.org]",
            "#REDIRECT [[記事名]]",
            "<!-- コメントアウトしたいテキスト -->",
            "11 <!-- 22 -->3<!-- 44 --> 5",
            "=== Level 2 ===",
            "====== Level 5 ======",
            "== Level err ==",
            "* に",
            "** に の いち",
            "*** に の いちti",
        ]
    i = 0
    for s in l:
        resultstr, i = remove_markup(s, i)
        print(resultstr)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()



