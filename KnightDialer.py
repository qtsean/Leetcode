class Solution:
    def knightDialer(self, n):
        if n == 1:
            return 10
        else:
            dp = {i:1 for i in range(10)}
            del dp[5]
            for i in range(n-1):
                zero = dp[4] + dp[6]
                one = dp[6] + dp[8]
                two = dp[7] + dp[9]
                three = dp[4] + dp[8]
                four = dp[0] + dp[3] + dp[9]
                six = dp[0] + dp[1] + dp[7]
                seven = dp[2] + dp[6]
                eight = dp[1] + dp[3]
                nine = dp[2] + dp[4]
                dp[0] = zero
                dp[1] = one
                dp[2] = two
                dp[3] = three
                dp[4] = four
                dp[6] = six
                dp[7] = seven
                dp[8] = eight
                dp[9] = nine
            return sum([v for k, v in dp.items()]) % (10**9 + 7)
