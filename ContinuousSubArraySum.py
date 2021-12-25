class Solution:
    def checkSubarraySum(self, nums, k):
        seen = {0: -1}
        prev = 0
        for i, n in enumerate(nums):
            prev = (prev + n) % k
            if prev in seen:
                if i - seen[prev] > 1:
                    return True
            else:
                seen[prev] = i
        return False
