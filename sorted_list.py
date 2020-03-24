# -*-coding: utf-8 -*-
# 实现有序列表


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


class OrderedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head()
        count = 0
        while current is not None:
            current = current.getNext()
            count += 1
        return count

    def isEmpty(self):
        return self.head is None

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            value = current.getData()
            if value == item:
                found = True
                break
            if item < value:
                found = False
                break
            current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        while current is not None:
            value = current.getData()
            if value >= item:
                break
            previous = current
            current = current.getNext()
        new_item = Node(item)
        if previous is None:
            new_item.setNext(self.head)
            self.head = new_item
        else:
            new_item.setNext(previous.getNext())
            previous.setNext(new_item)

    def remove(self, item):
        previous = None
        current = self.head
        while current is not None:
            if current.getData() == item:
                break
            previous = current
            current = current.getNext()
        if current is not None:
            if previous is None:
                self.head = self.head.getNext()
            else:
                previous.setNext(current.getNext())

    def printList(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

ol = OrderedList()
ol.add(1)
ol.add(3)
ol.add(4)
ol.add(2)

ol.printList()
print(ol.search(3))
ol.remove(3)
print(ol.search(3))
ol.printList()
ol.remove(2)
ol.printList()