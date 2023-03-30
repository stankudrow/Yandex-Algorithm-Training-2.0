#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28738/problems/A/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    value = int(input())
    maxval = value
    maxcount = 1 if value else 0
    while value:
        value = int(input())
        if value == maxval:
            maxcount += 1
        if value > maxval:
            maxval = value
            maxcount = 1
    print(maxcount)
