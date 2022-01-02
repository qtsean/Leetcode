class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(len(nums)):
            if j == 0:
                i += 1
            else:
                if nums[j] == nums[j-1]:
                    continue
                else:
                    nums[i] = nums[j]
                    i += 1
        return i