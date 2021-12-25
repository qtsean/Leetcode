from functools import lru_cache

# Back Track
class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        self.mem = {}
        return self.backTrack(0, len(nums) - 1, nums)

    def backTrack(self, left, right, nums):
        if (left, right) in self.mem:
            return self.mem[(left, right)]
        if left + 1 == right:
            return 0
        res = float('-inf')
        for mid in range(left+1, right):
            res = max(res,
                      self.backTrack(left, mid, nums) + self.backTrack(mid, right, nums) + nums[mid] * nums[
                          left] * nums[right])
        self.mem[(left, right)] = res
        return res

# DP
class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if i+1 == j:
                    dp[i][j] = 0
                else:
                    for k in range(i+1, j):
                        dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
        return dp[0][len(nums)-1]




s = Solution()
s.maxCoins([3,1,5,8])