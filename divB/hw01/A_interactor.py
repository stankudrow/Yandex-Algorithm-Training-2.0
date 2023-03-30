#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/A/"""


# pylint: disable=invalid-name
# pylint: disable=too-many-return-statements


def solve(ret: int, inter: int, check: int) -> int:
    """
    Return the final decision.

    Parameters
    ----------
    return_code : int
        -128 <= r <= 127.
    interactor_code : int
        0 <= i <= 7.
    checker_code : int
        0 <= c <= 7.

    Returns
    -------
    int

    """
    if inter == 0:
        if ret:
            return 3
        return check
    if inter == 1:
        return check
    if inter == 4:
        if ret:
            return 3
        return 4
    if inter == 6:
        return 0
    if inter == 7:
        return 1
    return inter


if __name__ == "__main__":
    ret_code, inter_code, check_code = (
        int(input()) for _ in range(3)
    )
    print(solve(ret_code, inter_code, check_code))
