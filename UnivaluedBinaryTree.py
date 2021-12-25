import collections
import copy
from math import sqrt


class Solution:
    def numSquarefulPerms(self, nums):
        neighbors = collections.defaultdict(set)
        total_number = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                n1 = nums[i]
                n2 = nums[j]
                if int(sqrt(n1 + n2))**2 == n1 + n2:
                    neighbors[n1].add(n2)
                    neighbors[n2].add(n1)
        counter = collections.Counter(nums)
        mem = set()
        self.ans = 0
        self.backTrack([], neighbors, mem, total_number, counter)
        return self.ans

    def backTrack(self, tmp, neighbors, mem, total_number, counter):
        if tuple(tmp) in mem:
            return
        if len(tmp) == total_number:
            self.ans += 1
            return
        if not tmp:
            for key in counter.keys():
                counter[key] -= 1
                self.backTrack([key], neighbors, mem, total_number, counter)
                counter[key] += 1
        else:
            last_number = tmp[-1]
            for neighbor in neighbors[last_number]:
                if counter[neighbor] > 0:
                    counter[neighbor] -= 1
                    tmp.append(neighbor)
                    self.backTrack(tmp, neighbors, mem, total_number, counter)
                    tmp.pop()
                    counter[neighbor] += 1
        mem.add(tuple(tmp))