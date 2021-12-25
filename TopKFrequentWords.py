import collections
import heapq


class Solution:
    def topKFrequent(self, words, k):
        counter = collections.Counter(words)
        heap = [[-v, k] for k, v in counter.items()]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
