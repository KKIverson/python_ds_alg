# -*-coding: utf-8 -*-
# 10进制转换为任意进制（stack实现）
from pythonds.basic.stack import Stack


def Dec2Base(num, base):
    s = Stack()
    baseSymbol = '0123456789ABCDEF'
    newNum = ''
    pos = 0
    while num > 0:
        num, rem = divmod(num, base)
        s.push(baseSymbol[rem])
    while not s.isEmpty():
        newNum += s.pop()
    return newNum

print(Dec2Base(20,16))