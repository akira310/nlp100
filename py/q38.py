# -*- coding: utf-8 -*-

import sys
import q36
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

def main():

    d = dict()
    for neko in q36.sort_neko():
        d[neko[1]] = 1 if neko[1] not in d else d[neko[1]]+1

    l = sorted(d.items(), key=lambda x: x[0])
    plt.bar(left=[x for x in range(len(l))],
            height=[y[1] for y in l])
            # tick_label=[y[0] for y in l])
    plt.show()


if __name__ == '__main__':
    main()
