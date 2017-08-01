# -*- coding:utf-8 -*-
# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

for m in range(168):
    for n in range(m):
        if m * m - n * n == 168:
            x = n * n - 100
            print x
