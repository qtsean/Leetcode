from functools import lru_cache


class Solution:
    def numDistinct(self, s, t):
        @lru_cache(None)
        def backTrack(index, used):
            if used == len(t):
                return 1
            if index == len(s):
                return 0
            res = 0
            res += backTrack(index+1, used)
            if s[index] == t[used]:
                res += backTrack(index+1, used+1)
            return res
        return backTrack(0, 0)

