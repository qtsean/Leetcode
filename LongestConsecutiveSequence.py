class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        used = set()
        ans = 0
        for n in s:
            if n in used:
                continue
            count = 0
            left = n - 1
            while left in s:
                used.add(left)
                count += 1
                left -= 1
            right = n + 1
            while right in s:
                used.add(right)
                right += 1
                count += 1
            ans = max(ans, count + 1)
        return ans