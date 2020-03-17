# -*-coding: utf-8 -*-
from pythonds.basic.stack import Stack
# 将中缀表达式转为后缀表达式（利用stack）

def priority(op):
    if op == '(':
        return 0
    elif op in "+-":
        return 1
    else:
        return 2

def mid2post(exp):
    expList = exp.split(' ')
    s = Stack()
    postList = []
    for v in expList:
        if v == '(':
            s.push(v)
        elif v == ')':
            top = s.pop()
            while top != '(':
                postList.append(top)
                top = s.pop()
        elif v in '+-*\\':
            while not s.isEmpty() and priority(v) <= priority(s.peek()):
                top = s.pop()
                postList.append(top)
            s.push(v)
        else:
            postList.append(v)
    while not s.isEmpty():
        postList.append(s.pop())
    return ' '.join(postList)


print(mid2post('( A + B ) * C - ( D - E ) * ( F + G )'))