import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
    def addNum(self, num: int) -> None:
        if not self.left or num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left) - len(self.right) == 2:
            cur = heapq.heappop(self.left)
            heapq.heappush(self.right, -cur)
        elif len(self.right) - len(self.left) == 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
