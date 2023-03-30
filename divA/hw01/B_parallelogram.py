#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28724/problems/B/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    for _ in range(int(input())):
        coords = list(
            map(int, input().split())
        )  # in an arbitrary order
        points = (
            (coords[i], coords[i + 1])
            for i in range(0, len(coords), 2)
        )
        p1, p2, p3, p4 = sorted(points)
        side1 = (p2[0] - p1[0], p2[1] - p1[1])
        side2 = (p3[0] - p1[0], p3[1] - p1[1])
        side3 = (p4[0] - p3[0], p4[1] - p3[1])
        side4 = (p4[0] - p2[0], p4[1] - p2[1])
        print(
            "YES"
            if (side1 == side3) and (side2 == side4)
            else "NO"
        )
