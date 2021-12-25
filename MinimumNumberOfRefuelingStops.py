import heapq


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        heap = []
        ans = 0
        tank = startFuel
        stations.append([target, 0])
        for s in stations:
            pos, fuel = s
            if pos > tank:
                while heap and pos > tank:
                    tank += -heapq.heappop(heap)
                    ans += 1
                if pos > tank:
                    return -1
            heapq.heappush(heap, -fuel)
        return ans