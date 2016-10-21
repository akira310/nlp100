# -*- coding: utf-8 -*-

import sys
import requests
import q25
import q28


def get_url(seed):
    url ="https://jp.wikipedia.org/w/api.php"
    payload = {
                "action": "query",
                "titles": "ファイル:{}".format(seed.replace(" ", "_")),
                "prop": "imageinfo",
                "format": "json",
                "iiprop": "url"
              }
    resp = requests.get(url, params=payload).json()
    try:
        for info in resp["query"]["pages"]["-1"]["imageinfo"]:
            if "url" in info:
                print(info["url"])
    except Exception as e:
        print(e)


def main():
    i = 0
    for k, v in q25.extract("国").items():
        if u"国旗画像" in k:
            get_url(q28.remove_markup(v, i)[0])

def test():
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test()
    else:
        main()
