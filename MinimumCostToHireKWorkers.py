import heapq


class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([[w/q, w, q] for w, q in zip(wage, quality)])
        ans = float('inf')
        sumq = 0
        heap = []
        for worker in workers:
            ratio, w, q = worker
            sumq += q
            heapq.heappush(heap, -q)
            if len(heap) > k:
                sumq += heapq.heappop(heap)
            if len(heap) == k:
                ans = min(ans, sumq * ratio)
        return ans