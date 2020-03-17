class Stack(object):
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        return self.items.pop()
    def peep(self):
        return self.items[-1]
    def push(self, value):
        self.items.append(value)

s = Stack()
s.push(10)
print(s.size())
print(s.pop())
print(s.isEmpty())