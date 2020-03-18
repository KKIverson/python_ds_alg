# -*- coding: utf-8 -*-
from pythonds.basic.deque import Deque
# 利用deque进行回文数检查


def cycleCheck(st):
    dq = Deque()
    for i in st:
        dq.addFront(i)
    isCyC = True
    while dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            isCyC = False
            break
    return isCyC


print(cycleCheck('rever'))
