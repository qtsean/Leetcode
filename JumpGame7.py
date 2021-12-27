class Solution:
    def canReach(self, s, minJump, maxJump):
        dp = [c == "0" for c in s]
        pre = 0
        for i in range(1, len(s)):
            if i >= minJump:
                pre += dp[i-minJump]
            if i > maxJump:
                pre -= dp[i-maxJump-1]
            dp[i] = dp[i] and pre > 0
        return dp[-1]