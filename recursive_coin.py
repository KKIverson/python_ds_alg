# -*-coding:utf-8-*-
# 采用递归方式求最小找零问题(存在大量的重复计算）


def recMC(coinValueList, change):
    minNum = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoin = 1 + recMC(coinValueList, change - i)
            if numCoin < minNum:
                minNum = numCoin
    return minNum


print(recMC([1, 5, 10, 25], 40))
