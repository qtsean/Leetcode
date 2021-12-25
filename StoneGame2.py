from functools import lru_cache


class Solution:
    def stoneGameII(self, piles):
        @lru_cache(None)
        def dfs(i, m, alice):
            if i == len(piles):
                return 0
            if alice:
                ans = 0
                for x in range(1, min(len(piles)-i, 2*m)+1):
                    ans = max(ans, sum(piles[i:i+x]) + dfs(i+x, max(m, x), not alice))
                return ans
            else:
                ans = float('inf')
                for x in range(1, min(len(piles)-i, 2*m)+1):
                    ans = min(ans, dfs(i+x, max(m, x), not alice))
                return ans
        return dfs(0, 1, True)