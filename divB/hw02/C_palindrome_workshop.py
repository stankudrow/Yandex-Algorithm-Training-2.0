#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28738/problems/C/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    string = input()
    price = 0
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            price += 1
        left += 1
        right -= 1
    print(price)
