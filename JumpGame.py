class Solution:
    def canJump(self, nums):
        far = 0
        for i, n in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + n)
        return True
                