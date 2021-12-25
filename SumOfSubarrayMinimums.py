class Solution:
    def sumSubarrayMins(self, arr):
        arr = [0] + arr + [0]
        stack = []
        ans = 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                k = stack.pop()
                j = stack[-1]
                ans += (k - j) * (i - k) * arr[k]
            stack.append(i)
        return ans % (10**9 + 7)
