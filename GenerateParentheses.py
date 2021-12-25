class Solution:
    def generateParenthesis(self, n):
        ans = []
        self.dfs(0, 0, n, ans, [])
        return ans

    def dfs(self, count_left, used_left, length, ans, tmp):
        if count_left == 0 and used_left == length:
            ans.append("".join(tmp))
            return
        if used_left < length:
            self.dfs(count_left+1, used_left+1, length, ans, tmp + ["("])
        if count_left > 0:
            self.dfs(count_left-1, used_left, length, ans, tmp+[")"])
