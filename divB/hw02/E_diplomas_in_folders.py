#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28738/problems/E/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    folders_total = int(input())
    folders = tuple(map(int, input().split()))
    summ, maxx = 0, folders[0]
    for folder in folders:
        summ += folder
        if folder > maxx:
            maxx = folder
    print(summ - maxx)
