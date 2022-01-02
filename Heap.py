'''
            0
        1       2
    3       4 5     6
'''


class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.initialize()

    def initialize(self):
        child = (len(self.heap) - 2) // 2
        while child >= 0:
            self.adjustDown(child)
            child -= 1

    def adjustDown(self, parent):
        child = parent * 2 + 1
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1
            if self.heap[child] < self.heap[parent]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                parent = child
                child = parent * 2 + 1
            else:
                break

    def adjustUp(self, child):
        parent = (child - 1) // 2
        while child > 0:
            if self.heap[parent] > self.heap[child]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                child = parent
                parent = (child - 1) // 2
            else:
                break

    def add(self, num):
        self.heap.append(num)
        self.adjustUp(len(self.heap)-1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.adjustDown(0)