class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.initialize()

    def initialize(self):
        child = (len(self.heap) - 2) // 2
        while child >= 0:
            self.adjustDown(child)
            child -= 1

    def adjustDown(self, node):
        parent = node
        child = node * 2 + 1
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1
            if self.heap[parent] > self.heap[child]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                parent = child
                child = parent * 2 + 1
            else:
                return

    def adjustUp(self, node):
        child = node
        parent = (child - 1) // 2
        while child != 0:
            if self.heap[child] < self.heap[parent]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = parent
                parent = (child - 1) // 2
            else:
                return

    def insertInHeap(self, value):
        self.heap.append(value)
        child = len(self.heap) - 1
        self.adjustUp(child)

    def removeInHeap(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.adjustDown(0)

    def print(self):
        print(self.heap)

1
arr = [53, 17, 78, 9, 45, 65, 87, 23, 31]
heap = Heap(arr)
heap.print()
heap.insertInHeap(4)
heap.print()
heap.removeInHeap()
heap.print()
heap.removeInHeap()
heap.print()

