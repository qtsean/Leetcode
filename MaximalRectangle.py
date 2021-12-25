class Solution:
    def maximalRectangle(self, matrix):
        ans = 0
        heights = [0 for i in range(len(matrix[0]) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            stack = [-1]
            for j in range(len(heights)):
                while heights[stack[-1]] > heights[j]:
                    index = stack.pop()
                    h = heights[index]
                    w = j - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(j)
        return ans