#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/C/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=too-many-boolean-expressions


def validate_date(day: int, month: int, year: int) -> bool:
    """
    Return True if the provided date is valid.

    Parameters
    ----------
    day : int
    month : int
    year : int

    Returns
    -------
    bool

    """
    if isinstance(year, int) and year > 0:
        if isinstance(month, int) and 1 <= month <= 12:
            # set day upper bound according to the month provided
            if month in (4, 6, 9, 11):
                upbound = 30
            elif month == 2:
                # check if a year is a leap/bissextile
                if (year % 4 == 0) and (
                    year % 100 != 0 or year % 400 == 0
                ):
                    upbound = 29
                else:
                    upbound = 28
            else:
                upbound = 31
            if 1 <= day <= upbound:
                return True
    return False


def solve(
    day_or_month: int, month_or_day: int, year: int
) -> int:
    """
    Return 1 if the date is uniquely determined, and 0 otherwise.

    If day and month values are exchangeable,
    the date matches both european and american formats.

    Parameters
    ----------
    day_or_month : int
        1 <= dom <= 31.
    month_or_day : int
        1 <= mod <= 31.
    year : int
        1970 <= year <= 2069.

    Returns
    -------
    int

    """
    date1 = day_or_month, month_or_day, year
    res1 = validate_date(*date1)
    date2 = month_or_day, day_or_month, year
    res2 = validate_date(*date2)
    return int(not (res1 and res2 and date1 != date2))


if __name__ == "__main__":
    dom, mod, year = (int(var) for var in input().split())
    print(solve(dom, mod, year))
