from functools import lru_cache


class Solution:
    def minCost(self, n, cuts):
        @lru_cache(None)
        def dfs(i, j):
            res = float('inf')
            for c in cuts:
                if i < c < j:
                    res = min(res, j - i + dfs(i, c) + dfs(c, j))
            if res == float("inf"):
                return 0
            else:
                return res
        return dfs(0, n)