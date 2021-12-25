class Solution:
    def singleNumber(self, nums):
        cur = nums[0]
        for i in range(1, len(nums)):
            cur = cur ^ nums[i]
        return cur