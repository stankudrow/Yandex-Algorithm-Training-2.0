#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28736/problems/A"""

# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name

from typing import List, Sequence


def confuse(seq: Sequence) -> List:
    """
    Return the list from the sequence as S - elem, where S = sum(seq).

    Parameters
    ----------
    seq: Sequence

    Returns
    -------
    List

    """
    summ = sum(seq)
    return [summ - elem for elem in seq]


if __name__ == "__main__":
    nelem, nconf = map(int, input().split())
    seq = list(map(int, input().split()))
    for _ in range(nconf):
        seq = confuse(seq)
    minn, maxx = seq[0], seq[0]
    for elem in seq:
        if elem < minn:
            minn = elem
        if elem > maxx:
            maxx = elem
    print(maxx - minn)
