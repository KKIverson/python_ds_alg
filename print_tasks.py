# -*-coding:utf-8-*-
import random
from pythonds.basic.queue import Queue
# 利用队列模拟打印机队列


class Task(object):
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randint(1, 20)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp


class Printer(object):
    def __init__(self, ppm):
        self.ppm = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def isBusy(self):
        return self.currentTask is not None

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def startNext(self, task):
        self.currentTask = task
        self.timeRemaining = task.getPages() / self.ppm * 60


def simulation(numberSeconds, ppm):
    printer = Printer(ppm=ppm)
    tasks = Queue()
    waitingList = []
    for currentTime in range(numberSeconds):
        if printer.isBusy():
            printer.tick()
        else:
            if not tasks.isEmpty():
                newTask = tasks.dequeue()
                printer.startNext(newTask)
                waitingList.append(newTask.waitTime(currentTime))
        if random.randint(1, 180) == 180:
            task = Task(currentTime)
            tasks.enqueue(task)

    print(sum(waitingList) * 1.0 / len(waitingList))


def main():
    for i in range(10):
        simulation(3600, 20)


if __name__ == '__main__':
    main()
