import collections
from functools import lru_cache


class Solution:
    def mostSimilar(self, n: int, roads, names, targetPath):
        neighbors = collections.defaultdict(list)
        for l, r in roads:
            neighbors[l].append(r)
            neighbors[r].append(l)
        mem = {}
        min_cost = float("inf")
        min_path = []
        for i in range(n):
            cost, path = self.dfs(i, neighbors, mem, 0, names, targetPath)
            if cost < min_cost:
                min_cost = cost
                min_path = path
        return min_path

    def dfs(self, node, neighbors, mem, index, names, targetPath):
        if index == len(targetPath):
            return 0, []
        if (index, node) in mem:
            return mem[(index, node)]
        min_cost = float('inf')
        min_path = []
        for neighbor in neighbors[node]:
            cost, path = self.dfs(neighbor, neighbors, mem, index+1, names, targetPath)
            if cost < min_cost:
                min_cost = cost
                min_path = path
        diff = 1 if names[node] != targetPath[index] else 0
        mem[(index, node)] = (min_cost+diff, [node] + min_path)
        return mem[(index, node)]