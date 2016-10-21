# -*- coding: utf-8 -*-

import sys
import q36
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    nekos = q36.sort_neko()

    plt.xscale("log")
    plt.yscale("log")
    plt.plot([x for x in range(len(nekos))], [y[1] for y in nekos], '.')
    plt.show()


if __name__ == '__main__':
    main()
