#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/B/"""


# pylint: disable=invalid-name
# pylint: disable=too-many-boolean-expressions


if __name__ == "__main__":
    stations, instation, outstation = (
        int(var) for var in input().split()
    )
    diff1 = (outstation - instation) % stations
    diff2 = (instation - outstation) % stations
    print(min(diff1, diff2) - 1)
