import heapq


class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        engineers = [[s, e] for s, e in zip(speed, efficiency)]
        engineers.sort(key=lambda x: x[1], reverse=True)
        heap = []
        sum_speed = 0
        ans = 0
        for s, e in engineers:
            heapq.heappush(heap, s)
            sum_speed += s
            if len(heap) > k:
                sum_speed -= heapq.heappop(heap)
            ans = max(ans, sum_speed * e)
        return ans % (10**9 + 7)