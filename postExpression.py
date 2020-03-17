# -*-coding: utf-8 -*-
from pythonds.basic.stack import Stack
# 计算后缀表达式的结果


def posExpCompute(exp):
    s = Stack()
    expList = exp.split(' ')
    pos = 0
    while pos < len(expList):
        value = expList[pos]
        if value in '+-*/':
            a = s.pop()
            b = s.pop()
            s.push(compute(int(b), int(a), value))
        else:
            s.push(value)
        pos += 1
    return s.pop()


def compute(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b


print(posExpCompute('7 8 + 3 2 + /'))
