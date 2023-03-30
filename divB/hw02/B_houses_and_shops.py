#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28738/problems/B/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    seq = input().replace(" ", "")
    maxdist = 0
    if seq:
        left, right = 0, len(seq) - 1
        for pos, building in enumerate(seq):
            if building == "1":
                lpos = max(left, pos - 1)
                rpos = min(right, pos + 1)
                ishop = 0
                while left <= lpos < rpos <= right:
                    if seq[lpos] == "2":
                        ishop = lpos
                        break
                    if seq[rpos] == "2":
                        ishop = rpos
                        break
                    lpos = max(left, lpos - 1)
                    rpos = min(right, rpos + 1)
                maxdist = max(maxdist, abs(pos - ishop))
    print(maxdist)
