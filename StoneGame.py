from functools import lru_cache


class Solution:
    def stoneGame(self, piles):
        @lru_cache(None)
        def dp(i, j, player):
            if i > j:
                return 0
            if player == 0:
                return max(piles[i] + dp(i+1, j, 1), piles[j] + dp(i, j-1, 1))
            else:
                return min(-piles[i] + dp(i+1, j, 0), -piles[j] + dp(i, j-1, 0))
        return dp(0, len(piles)-1, 0) > 0