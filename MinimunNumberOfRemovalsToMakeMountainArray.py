import bisect


class Solution:
    def minimumMountainRemovals(self, nums):
        arr = [float('inf') for i in range(len(nums))]
        left_longest_increase = [0 for i in range(len(nums))]
        right_longest_increase = [0 for i in range(len(nums))]
        for i, n in enumerate(nums):
            index = bisect.bisect_left(arr, n)
            left_longest_increase[i] = index if index > 0 else -len(nums)
            arr[index] = n
        arr = [float('inf') for i in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            index = bisect.bisect_left(arr, n)
            right_longest_increase[i] = index if index > 0 else -len(nums)
            arr[index] = n
        ans = float('inf')
        for i in range(1, len(nums)-1):
            ans = min(ans, len(nums) - left_longest_increase[i] - right_longest_increase[i] - 1)
        return ans

s = Solution()
s.minimumMountainRemovals([100,92,89,77,74,66,64,66,64])