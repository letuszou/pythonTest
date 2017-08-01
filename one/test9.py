# -*- coding:utf-8 -*-
# 暂停一秒输出。

import time

for i in range(60):
    if i >= 60:
        exit()
    else:
        time.sleep(1)
        print i
