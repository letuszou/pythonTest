# -*- coding:utf-8 -*-
# 斐波那契数列。

def count(number):
    if number == 1 or number == 2:
        return 1
    else:
        return count(number - 1) + count(number - 2)

print count(10)