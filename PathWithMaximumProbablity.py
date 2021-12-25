import collections
import heapq
import math


class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        neighbors = collections.defaultdict(list)
        distance = {}
        weights = [-math.log2(x) for x in succProb]
        pair_weights = {}
        for edge, weight in zip(edges, weights):
            left, right = edge
            neighbors[left].append(right)
            neighbors[right].append(left)
            pair_weights[(left, right)] = weight
            pair_weights[(right, left)] = weight
        heap = [[0, start]]
        while heap:
            cur_dist, node = heapq.heappop(heap)
            if node in distance:
                continue
            distance[node] = cur_dist
            for neighbor in neighbors[node]:
                if neighbor not in distance:
                    heapq.heappush(heap, [cur_dist+pair_weights[(node, neighbor)], neighbor])
        if end in distance:
            return 2 ** (-distance[end])
        else:
            return 0