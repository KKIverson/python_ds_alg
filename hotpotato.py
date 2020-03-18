# -*-coding:utf-8-*-
from pythonds.basic.queue import Queue
# 利用队列实现约瑟夫环（或者烫手山芋游戏）


def hotpotato(nameList, num):
    q = Queue()
    for i in nameList:
        q.enqueue(i)
    while q.size() > 1:
        for _ in range(num):
            v = q.dequeue()
            q.enqueue(v)
        print(q.dequeue())
    print(f"the last one is: {q.dequeue()}")


hotpotato(['Allen', 'Kobe', "Kevin", 'Paul', 'James'], 7)
