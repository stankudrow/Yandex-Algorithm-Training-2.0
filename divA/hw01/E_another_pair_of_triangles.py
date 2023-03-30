#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28724/problems/E/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    p = int(input())
    # the sides of a triangle should be integer
    if p > 2:
        a = p // 3
        b = (p - a) // 2
        c = p - (a + b)
        if a + b > c:
            print(a, b, c)
            d = 1 if p % 2 else 2
            e = (p - d) // 2
            f = p - (d + e)
            print(d, e, f)
        else:
            print(-1)
