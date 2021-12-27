import heapq


class MKAverage:

    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.large = []
        self.small = []
        self.s = 0
        self.count = 0

    def addElement(self, num):
        self.count += 1
        if self.count >= self.m:
            if num <= -self.small[0]:
                self.s -= heapq.heappushpop(self.small, -num)
            else:
                self.s += heapq.heappushpop(self.large, num)
        else:
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, num)
            if len(self.small) > self.k:
                heapq.heappop(self.small)
            if len(self.large) > self.k:
                heapq.heappop(self.large)

    def calculateMKAverage(self):
        if self.count < self.m:
            return -1
        return int(self.s / (self.count - 2 * self.k))