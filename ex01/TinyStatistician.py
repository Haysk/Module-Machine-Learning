# coding:utf-8

import numpy as np
import math


class TinyStatistician:

    def mean(x):
        if (not len(x) or
                not (isinstance(x, list) or isinstance(x, np.ndarray))):
            return None
        result = 0
        for value in x:
            result = result + value
        return result / len(x)

    def median(x):
        if (not len(x) or
                not (isinstance(x, list) or isinstance(x, np.ndarray))):
            return None
        x.sort()
        size = len(x)
        if (size % 2 == 1):
            return x[int((size + 1) / 2) - 1]
        return (x[int(size / 2 - 1)] + x[int(size / 2)]) / 2

    def quartile(x):
        if (not len(x) or
                not (isinstance(x, list) or isinstance(x, np.ndarray))):
            return None
        size = len(x)
        first_quartile = 0
        rank = (size + 3) / 4
        print(rank)
        floor_rank = math.floor(rank)
        ceil_rank = math.ceil(rank)
        if (rank % 1 == 0.25):
            first_quartile = \
                (3 * x[floor_rank - 1] + x[ceil_rank - 1]) / 4
        elif (rank % 1 == 0.5):
            first_quartile = \
                (x[floor_rank - 1] + x[ceil_rank - 1]) / 2
        elif (rank % 1 == 0.75):
            first_quartile = \
                (x[floor_rank - 1] * 3 + x[ceil_rank - 1]) / 4
        else:
            first_quartile = x[int(rank) - 1]

        third_quartile = 0
        rank = (3 * size + 1) / 4
        floor_rank = math.floor(rank)
        ceil_rank = math.ceil(rank)
        if (rank % 1 == 0.25):
            third_quartile = \
                (3 * x[floor_rank - 1] + x[ceil_rank - 1]) / 4
        elif (rank % 1 == 0.5):
            third_quartile = \
                (x[floor_rank - 1] + x[ceil_rank - 1]) / 2
        elif (rank % 1 == 0.75):
            third_quartile = \
                (x[floor_rank - 1] * 3 + x[ceil_rank - 1]) / 4
        else:
            third_quartile = x[int(rank) - 1]

        return [first_quartile, third_quartile]

    def percentile(x, p):
        if (not len(x) or
                not (isinstance(x, list) or isinstance(x, np.ndarray))):
            return None
        size = len(x)
        result = 0
        rank = (p / 100 * (size))
        print(rank)
        if (rank % 1 != 0.0):
            floor_rank = math.floor(rank)
            ceil_rank = math.ceil(rank)
            result = \
                (x[floor_rank] + x[ceil_rank]) / 2
        else:
            result = x[int(rank) - 1]
        return result

    def var(x):
        if (not len(x) or
                not (isinstance(x, list) or isinstance(x, np.ndarray))):
            return None

    def std(x):
        if (not len(x) or
                not (isinstance(x, list) or isinstance(x, np.ndarray))):
            return None
