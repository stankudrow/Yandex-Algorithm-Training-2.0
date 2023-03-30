#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/E/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    leg = int(input())  # of a right triangle
    xc, yc = map(int, input().split())
    if (
        (0 <= xc <= leg)
        and (0 <= yc <= leg)
        and (yc <= -xc + leg)
    ):
        print(0)
    else:
        half = leg // 2
        if (xc <= half) and (yc <= half):
            print(1)
        if (xc > half) and (yc <= xc):
            print(2)
        if (yc > half) and (yc > xc):
            print(3)
