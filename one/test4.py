# -*- coding:utf-8 -*-
# 输入某年某月某日，判断这一天是这一年的第几天？

p = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("请输入年"))
month = int(input("请输入月"))
days = int(input("请输入日"))

if year % 4 == 0:
    months = m[:month - 1]
    months = sum(months)
    print months + days
