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


def print_number(numbers):
    """表示する文字列を生成するジェネレータ

    numbers : list(int)
        処理対象の数値のリスト
    """
    for n in numbers:
        mark = '*' if is_marked_number(n) else ''
        yield str(n) + mark


def print_numbers():
    """1〜40の数字を表示する

    ジェネレータを使って実装
    """

    for line in print_number(range(1, 40 + 1)):
        print(line)


if __name__ == '__main__':
    print_numbers()
