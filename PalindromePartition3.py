from functools import lru_cache


class Solution:
    def palindromePartition(self, s, k):
        @lru_cache(None)
        def dfs(i, k):
            if k == 1:
                return cost(i, len(s) - 1)
            if len(s) - i == k:
                return 0
            if len(s) - i < k:
                return float('inf')
            res = float('inf')
            for j in range(i, len(s)-1):
                res = min(res, dfs(j+1, k-1) + cost(i, j))
            return res


        @lru_cache(None)
        def cost(left, right):
            count = 0
            while left < right:
                if s[left] != s[right]:
                    count += 1
                left += 1
                right -= 1
            return count

        return dfs(0, k)
