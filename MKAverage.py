import heapq
from collections import deque
from sortedcontainers import SortedList


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.total = 0
        self.small = 0
        self.large = 0
        self.nums = deque()
        self.sorted_nums = SortedList()
    def addElement(self, num: int) -> None:
        self.total += num
        self.nums.append(num)
        index = self.sorted_nums.bisect_left(num)
        if index < self.k:
            self.small += num
            if len(self.sorted_nums) >= self.k:
                self.small -= self.sorted_nums[self.k-1]
        if index >= len(self.sorted_nums) - self.k + 1:
            self.large += num
            if len(self.sorted_nums) >= self.k:
                self.large -= self.sorted_nums[-self.k]
        self.sorted_nums.add(num)

        if len(self.sorted_nums) > self.m:
            remove_number = self.nums.popleft()
            self.total -= remove_number
            index = self.sorted_nums.bisect_left(remove_number)
            if index < self.k:
                self.small -= remove_number
                self.small += self.sorted_nums[self.k]
            elif index >= len(self.sorted_nums) - self.k:
                self.large -= remove_number
                self.large += self.sorted_nums[-self.k-1]
            self.sorted_nums.remove(remove_number)
    def calculateMKAverage(self) -> int:
        if len(self.sorted_nums) < self.m:
            return -1
        return (self.total - self.small - self.large) // (self.m - 2 * self.k)