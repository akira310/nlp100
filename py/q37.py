# -*- coding: utf-8 -*-

import sys
import q36
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

def main():

    top10 = q36.sort_neko()[:10]

    for font in fm.findSystemFonts():
        if "ipag" in font:
            break
    fp = fm.FontProperties(fname=font, size=14)

    plt.bar(left=[x for x in range(len(top10))],
             height=[y[1] for y in top10],
             tick_label=[y[0] for y in top10])
    plt.xticks(fontproperties=fp)
    plt.show()


if __name__ == '__main__':
    main()
