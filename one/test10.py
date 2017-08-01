# -*- coding:utf-8 -*-
# 格式化当前时间

import time


def myTime():
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


myTime()
