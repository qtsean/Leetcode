class Solution:
    def jump(self, nums):
        jmp = 0
        far = 0
        cur_far = 0
        for i, n in enumerate(nums):
            if i > far:
                far = cur_far
                jmp += 1
            cur_far = max(cur_far, i + n)
        return jmp

s = Solution()
s.jump([2,3,1,1,4])