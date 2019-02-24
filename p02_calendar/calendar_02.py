#! /usr/local/bin/python3

"""
calendar_02.py
カレンダーを表示するスクリプト その2
Copyright (C) 2019 J.Kawahara
2019.2.24 J.Kawahara 新規作成
"""

import datetime
import sys

def is_leap_year(year):
    """指定された年は閏年か？

    Parameters
    ----------
    year : int
        対象の年
    
    Returns
    -------
    boolean
        指定された年が閏年の場合はTrue
    """
    # 閏年の定義
    # 400で割り切れる、または100で割り切れなく4で割り切れる年
    return ((year % 400) == 0) or \
        ((year % 100) != 0 and (year % 4) == 0)


def last_day_of_month(year, month):
    """指定された年月の最終日を取得する

    正攻法バージョン

    Parameters
    ----------
    year : int
        対象の年
    month : int
        対象の月
    
    Returns
    -------
    int
        指定された年月の最終日
    """
    
    if month != 2:
        if month in [4, 6, 9, 11]:
            return 30
        return 31
    
    # 2月が指定された場合
    # 指定された年がうるう年かどうかを判断する
    if is_leap_year(year):
        return 29
    return 28


def last_day_of_month_easy(year, month):
    """指定された年月の最終日を取得する

    お手軽バージョン

    Parameters
    ----------
    year : int
        対象の年
    month : int
        対象の月
    
    Returns
    -------
    int
        指定された年月の最終日
    """

    # 指定された年月の28日に4日を足して、
    # 得られた日付の「日」の値を引く。
    # 例）
    # 2019年4月28日 + 4日 = 2019年5月 2日
    # 2019年5月 2日 - 2日 = 2019年4月30日

    next_month = datetime.date(year, month, 28) + datetime.timedelta(days=4)
    last_date = next_month - datetime.timedelta(days=next_month.day)
    return last_date.day

    
def print_calendar(year, month):
    """カレンダーを表示する

    Parameters
    ----------
    year : int
        表示する年
    month : int
        表示する月
    """

    # 初日の曜日を取得する
    # weekday() 関数は月曜が0、日曜が6なので、
    # 日曜を0、土曜を6　に変換する
    first_date = datetime.date(year, month, 1)
    first_days_week = (first_date.weekday() + 1) % 7

    # 最終日を取得する
    # last_day = last_day_of_month(year, month)
    last_day = last_day_of_month_easy(year, month)

    # 見出しを表示する
    print("{0}年{1}月".format(year, month))
    print("日 月 火 水 木 金 土")

    # 初日までの空欄を作成する
    line = ''
    if first_days_week >0:
        line += '  '
        line += ('   ' * (first_days_week - 1))

    # カレンダーを表示する
    w = first_days_week
    for d in range(1, last_day + 1):
        if w > 0:
            line += ' '
        if d < 10:
            line += ' '
        
        line += str(d)

        if w >= 6:
            print(line)
            line = ''
        
        w = (w + 1) % 7
    
    if line != '':
        print(line)

    print()


def print_usage():
    """このスクリプトの説明を表示して終了する

    """
    print('usage: calendar_02.py [month] [year]')
    print('    month: 月 (1～12)')
    print('    year: 年 (1～9999)')
    print()
    exit()


if __name__ == '__main__':
    args = sys.argv
    current_date = datetime.date.today()
    year = current_date.year
    month = current_date.month

    # 実行時引数をチェックする
    # 「月」を取得する
    if len(args) >= 2:
        if args[1].isdecimal():
            month = int(args[1])
        else:
            print_usage()

    if not (1 <= month <= 12):
        print('月の値は、1～12の間で指定してください。')
        print_usage()

    # 「年」を取得する
    if len(args) >= 3:
        if args[2].isdecimal():
            year = int(args[2])
        else:
            print_usage()

    if not (1 <= year <= 9999):
        print('年の値は、1～9999の間で指定してください。')
        print_usage()
    
    print_calendar(year, month)
