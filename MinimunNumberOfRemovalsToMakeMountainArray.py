import bisect


class Solution:
    def minimumMountainRemovals(self, nums):
        arr = [float('inf') for n in nums]
        left = [0 for n in nums]
        right = [0 for n in nums]
        for i, n in enumerate(nums):
            index = bisect.bisect_left(arr, n)
            left[i] = index if index > 0 else -len(nums)
            arr[index] = n
        arr = [float('inf') for n in nums]
        for i in range(len(nums)-1, -1, -1):
            index = bisect.bisect_left(arr, nums[i])
            right[i] = index if index > 0 else -len(nums)
            arr[index]=  nums[i]

        ans = float("inf")
        for i in range(len(nums)):
            ans = min(ans, len(nums) - left[i] - right[i] - 1)
        return ans