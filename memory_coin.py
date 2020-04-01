# 将中间结果记录下来，避免多次重复计算（缓存+递归方式，非动态规划）
def recDC(coinValueList, change, knownResults):
    minNum = change
    if change in coinValueList:
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoin = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoin < minNum:
                minNum = numCoin
        knownResults[change] = minNum
    return minNum


print(recDC([1, 5, 10, 25], 63, [0] * 64))
