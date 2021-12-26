from functools import lru_cache


class Solution:
    def maxJumps(self, arr, d):
        @lru_cache(None)
        def dfs(i):
            res = 1
            for j in range(i-1, i-d-1, -1):
                if 0 <= j:
                    if arr[j] >= arr[i]:
                        break
                    else:
                        res = max(res, 1 + dfs(j))
            for j in range(i+1, i+d+1):
                if j < len(arr):
                    if arr[j] >= arr[i]:
                        break
                    else:
                        res = max(res, 1 + dfs(j))
            return res
        ans = 0
        for index in range(len(arr)):
            ans = max(ans, dfs(index))
        return ans
