# coding=utf-8
"""
Python练习实例4

题目：输入某年某月某日，判断这一天是这一年的第几天？
分析：
1.首先要判断输入的年月日是否合法；
2.判断该年是平年还是闰年；
3.对天数进行求和。

"""


# 判断平年闰年
def is_leap_year(_year):
    if (_year % 4 == 0 and _year % 100 != 0) or (_year % 400 == 0):
        return 1
    else:
        return 0


exit_flag = ''
while exit_flag != 'q':
    # 获取输入参数
    year = input("请输入年份：\n")
    month = input("请输入月份：\n")
    day = input("请输入日期：\n")

    is_leap = 0

    # 对输入的年月日进行合法性检查
    # 年份检查
    if year.isdigit() and int(year) > 0:
        year = int(year)
        is_leap = is_leap_year(year)
    else:
        print("年份输入错误，请重新输入一个正整数")
        continue

    # 月份检查
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month)
    else:
        print("月份输入错误，请重新输入一个1到12的正整数")
        continue

    print(is_leap)
    # 日期检查
    if day.isdigit() and 1 <= int(day) <= 31:
        day = int(day)

        if is_leap == 1 and month == 2 and day > 29:
            print("日期输入错误，%d是闰年，请重新输入一个1到29的正整数" % year)
            continue

        if is_leap == 0 and month == 2 and day > 28:
            print("日期输入错误，%d是平年，请重新输入一个1到28的正整数" % year)
            continue

    else:
        print("日期输入错误，请重新输入一个1到31的正整数")
        continue

    exit_flag = input("退出请输入q，任意键继续！\n").lower()
