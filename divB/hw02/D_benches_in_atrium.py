#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28738/problems/D/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    bench_len, blocks_num = map(int, input().split())
    positions = [int(pos) for pos in input().split()]
    centre, is_odd = divmod(bench_len, 2)
    for i, pos in enumerate(positions):
        if pos >= centre:
            if is_odd and pos == centre:
                print(centre)
            else:
                print(positions[i - 1], pos)
            break
