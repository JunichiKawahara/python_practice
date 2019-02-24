#! /usr/local/bin/python3

"""
x3_03.py
1~40を表示するスクリプト その3
Copyright (C) 2019 J.Kawahara
2019.2.21 J.Kawahara 新規作成
"""


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

    return (n % 3) == 0


def print_numbers():
    """1〜40の数字を表示する

    while ステートメントで実装
    """

    n = 1
    while n <= 40:
        mark = '*' if is_marked_number(n) else ''
        print(str(n) + mark)
        n += 1

if __name__ == '__main__':
    print_numbers()
