class Solution:
    def longestIncreasingPath(self, matrix):
        self.mem = {}
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs(i, j, matrix, -1))
        return ans

    def dfs(self, i, j, matrix, prev):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prev:
            return 0
        if (i, j) in self.mem:
            return self.mem[(i, j)]
        res = 1 + max(self.dfs(i-1, j, matrix, matrix[i][j]), self.dfs(i+1, j, matrix, matrix[i][j]), self.dfs(i, j-1, matrix, matrix[i][j]), self.dfs(i, j+1, matrix, matrix[i][j]))
        self.mem[(i, j)] = res
        return res

s = Solution()
s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])