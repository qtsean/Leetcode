from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes):
        @lru_cache(None)
        def dfs(l, r, k):
            if l > r:
                return 0
            count = 0
            while l + count <= r and boxes[l] == boxes[l + count]:
                count += 1
            l2 = l + count
            res = dfs(l2, r, 0) + (k + count) ** 2
            for m in range(l2, r+1):
                if boxes[m] == boxes[l]:
                    res = max(res, dfs(l2, m-1, 0) + dfs(m, r, k + count))
            return res
        return dfs(0, len(boxes) - 1, 0)