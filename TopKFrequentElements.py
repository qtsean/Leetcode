import collections
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        counter = [[-v, key] for key, v in counter.items()]
        heapq.heapify(counter)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(counter)[1])
        return ans
