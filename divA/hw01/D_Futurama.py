#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28724/problems/D/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from typing import List


def swap(bodies: List, body1: int, body2: int) -> int:
    """Print and swap bodies with the second body returned."""
    print(body1, body2)
    bodies[body1], bodies[body2] = bodies[body2], bodies[body1]
    return bodies[body2]


if __name__ == "__main__":
    nbodies, exchanges = map(int, input().split())
    if (4 <= nbodies <= 20) and (1 <= exchanges <= 100):
        bodies = list(range(nbodies + 1))
        for _ in range(exchanges):
            body1, body2 = map(int, input().split())
            bodies[body1], bodies[body2] = (
                bodies[body2],
                bodies[body1],
            )
        for i in range(1, nbodies - 1):
            if bodies[i] != i:
                current = i
                while bodies[current] != i:
                    current = swap(bodies, current, nbodies - 1)
                current = swap(bodies, current, nbodies)
                current = swap(bodies, current, nbodies)
                swap(bodies, bodies[nbodies - 1], nbodies - 1)
        if bodies[nbodies - 1] == nbodies:
            swap(bodies, nbodies - 1, nbodies)
