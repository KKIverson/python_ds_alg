# -*- coding: utf-8 -*-
# 动态规划解决找零问题(顺便将路径打印出来)


def dpMakechange(coinValueLists, change):
    minNum = [0] * (change + 1)
    centPath = [1] * (change + 1)
    for cents in range(change + 1):
        minNum[cents] = cents
        for i in [c for c in coinValueLists if c <= cents]:
            if minNum[cents - i] + 1 < minNum[cents]:
                minNum[cents] = minNum[cents - i] + 1
                centPath[cents] = i
    left = change
    while left > 0:
        print(centPath[left], end=' ')
        left = left - centPath[left]
    return minNum[change]


print(dpMakechange([1, 5, 10, 25], 75))