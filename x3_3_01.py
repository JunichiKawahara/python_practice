#! /usr/local/bin/python3

"""
x3_02.py
世界のナベアツスクリプト
Copyright (C) 2019 J.Kawahara
2019.2.21 J.Kawahara 新規作成
"""

import re


def is_has3_01(n):
    """
    「3」のつく数字か？

    1桁目が3かどうかをチェックする。
    「10で割る」〜「1桁目のチェック」を繰り返す。

    Parameters
    ----------
    n : int
        チェック対象の数値

    Returns
    -------
    bool
        「3」のつく数字の場合はTrue
    """

    x = n
    while x > 0:
        if (x % 10) == 3:
            return True
        x //= 10
    return False


def is_has3_02(n):
    """
    「3」のつく数字か？

    文字列に変換してから、1文字ずつチェックする

    Parameters
    ----------
    n : int
        チェック対象の数値

    Returns
    -------
    bool
        「3」のつく数字の場合はTrue
    """

    str_n = str(n)
    for c in str_n:
        if c == '3':
            return True
    return False


def is_has3_03(n):
    """
    「3」のつく数字か？

    正規表現を使ってチェック

    Parameters
    ----------
    n : int
        チェック対象の数値

    Returns
    -------
    bool
        「3」のつく数字の場合はTrue
    """
    return re.match('3', str(n)) is not None


def is_marked_number(n):
    """マークが必要な数値か？

    Parameters
    ----------
    n :int
        チェック対象の数値

    Returns
    -------
    bool
        マークが必要な数値の場合はTrue
    """

    # return ((n % 3) == 0 or is_has3_01(n))
    # return ((n % 3) == 0 or is_has3_02(n))
    return ((n % 3) == 0 or is_has3_03(n))


def print_numbers():
    """1〜40の数字を表示する

    for ステートメントで実装
    """

    for n in range(1, 40 + 1):
        mark = '*' if is_marked_number(n) else ''
        print(str(n) + mark)


if __name__ == '__main__':
    print_numbers()
