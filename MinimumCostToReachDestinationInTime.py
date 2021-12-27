import collections
import heapq


class Solution:
    def minCost(self, maxTime, edges, passingFees):
        neighbors = collections.defaultdict(list)
        times = {}
        for edge in edges:
            l, r, t = edge
            neighbors[l].append(r)
            neighbors[r].append(l)
            if (l, r) in times:
                times[(l, r)] = min(times[(l, r)], t)
                times[(r, l)] = min(times[(r, l)], t)
            else:
                times[(l, r)] = t
                times[(r, l)] = t
        visited = {}
        pq = [[passingFees[0], 0, 0]]    # cost, time, node
        while pq:
            cost, time, node = heapq.heappop(pq)
            if time > maxTime:
                continue
            if node == len(passingFees) - 1:
                return cost
            if node not in visited or visited[node] > time:
                visited[node] = time
                for neighbor in neighbors[node]:
                    heapq.heappush(pq, [cost+passingFees[neighbor], time+times[(node, neighbor)], neighbor])

        return -1