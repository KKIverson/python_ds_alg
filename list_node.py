# -*-coding: utf-8 -*-
# 用链表实现无重复项的无序列表


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, nex):
        self.next = nex

    def getData(self):
        return self.data

    def setData(self, v):
        self.data = v


class UnsortedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.getNext()
            count += 1
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
