class Solution:
    def countDigitOne(self, n):
        if n == 0:
            return 0
        ans = 0
        base = 1
        while base <= n:
            left = n // base // 10
            cur = n // base % 10
            right = n % base
            if cur > 1:
                ans += (left + 1) * base
            elif cur == 1:
                ans += left * base + right + 1
            else:
                ans += left * base
            base *= 10
        return ans