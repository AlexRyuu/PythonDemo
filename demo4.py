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


# 获取输入参数
year = int(input("请输入年份：\n"))
month = int(input("请输入月份：\n"))
day = int(input("请输入日期：\n"))

# 对输入的年月日进行合法性检查
