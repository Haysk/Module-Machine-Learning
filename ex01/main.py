# coding:utf-8

import numpy as np
from TinyStatistician import TinyStatistician as ts


def ex():
    x = np.arange(0, 1001)
    y = np.arange(0, 1000)
    z = [1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61]

    print("mean:")
    print("x:", ts.mean(x))
    print("y:", ts.mean(y))
    print("z:", ts.mean(z))
    print("\nmedian:")
    print("x:", ts.median(x))
    print("y:", ts.median(y))
    print("z:", ts.median(z))
    print("\nquartile:")
    print("x:", ts.quartile(x))
    print("y:", ts.quartile(y))
    print("z:", ts.quartile(z))
    print("\npercentile:")
    print("x:", ts.percentile(x, 25))
    print("y:", ts.percentile(y, 25))
    print("z:", ts.percentile(z, 25))
    print("x:", ts.percentile(x, 50))
    print("y:", ts.percentile(y, 50))
    print("z:", ts.percentile(z, 50))
    print("x:", ts.percentile(x, 75))
    print("y:", ts.percentile(y, 75))
    print("z:", ts.percentile(z, 75))
    # ts.TinyStatistician.mean(x)
    # ts.TinyStatistician.mean(y)
    # ts.TinyStatistician.mean(z)


if __name__ == "__main__":
    SystemExit(ex())
