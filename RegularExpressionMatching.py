class Solution:
    def isMatch(self, s, p):
        s = "#" + s
        p = "#" + p
        dp = [[False for i in range(len(p))] for j in range(len(s))]
        dp[0][0] = True
        for i in range(1, len(p)):
            if p[i] == "*":
                dp[0][i] = dp[0][i-2]
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[j] == "." or p[j] == s[i]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*" and (dp[i][j-2] or (dp[i-1][j] and (p[j-1] == "." or p[j-1] == s[i]))):
                    dp[i][j] = True
        return dp[-1][-1]