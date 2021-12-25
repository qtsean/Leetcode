class Solution:
    def longestOnes(self, nums, k):
        left = 0
        count = 0
        ans = 0
        for n in nums:
            if n == 1:
                count += 1
            elif n == 0 and k > 0:
                count += 1
                k -= 1
            elif n == 0 and k == 0:
                while k == 0:
                    if nums[left] == 0:
                        k += 1
                        left += 1
                    else:
                        count -= 1
                        left += 1
                k -= 1
            ans = max(ans, count)
        return ans
