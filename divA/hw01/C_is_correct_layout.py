#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28724/problems/C/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=simplifiable-if-expression


def sanitize_input() -> list[list[int]]:
    """Returns the validated tic-tac-toe board."""
    board = []
    for _ in range(3):
        row = list(map(int, input().split()))
        if len(row) != 3 or not (set(row) <= {0, 1, 2}):
            raise ValueError(f"{row} is an invalid row.")
        board.append(row)
    return board


def is_winner(board: list[list[int]], player: int) -> bool:
    """Returns True if player has a winning sequence."""
    rows, cols = True, True
    main_diag, side_diag = True, True
    for idx in range(3):
        if board[idx][idx] != player:
            main_diag = False
        if board[idx][2 - idx] != player:
            side_diag = False
        rows, cols = True, True
        for jdx in range(3):
            if board[idx][jdx] != player:
                rows = False
            if board[jdx][idx] != player:
                cols = False
        if rows or cols:
            return True
    return main_diag or side_diag


def is_correct_layout(board: list[list[int]]) -> bool:
    """Returns True if the layout is possible, i.e. is correct."""
    win1, win2 = is_winner(board, 1), is_winner(board, 2)
    ones, twos = 0, 0
    for row in board:
        for item in row:
            if item == 1:
                ones += 1
            if item == 2:
                twos += 1
    if win1 and win2:
        return False
    if win1 and ones - twos != 1:
        return False
    if win2 and twos - ones != 0:
        return False
    return True if -1 < ones - twos < 2 else False


if __name__ == "__main__":
    board = sanitize_input()
    print("YES" if is_correct_layout(board) else "NO")
