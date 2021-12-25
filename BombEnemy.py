class Solution:
    def maxKilledEnemies(self, grid):
        left2right = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        right2left = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        up2bottom = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        bottom2top = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid[0])):
                if grid[i][j] == "W":
                    count = 0
                if grid[i][j] == "E":
                    count += 1
                left2right[i][j] = count
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == "W":
                    count = 0
                if grid[i][j] == "E":
                    count += 1
                right2left[i][j] = count
        for j in range(len(grid[0])):
            count = 0
            for i in range(len(grid)):
                if grid[i][j] == "W":
                    count = 0
                if grid[i][j] == "E":
                    count += 1
                up2bottom[i][j] = count
        for j in range(len(grid[0])):
            count = 0
            for i in range(len(grid)-1, -1, -1):
                if grid[i][j] == "W":
                    count = 0
                if grid[i][j] == "E":
                    count += 1
                bottom2top[i][j] = count
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    ans = max(ans, left2right[i][j] + right2left[i][j] + up2bottom[i][j] + bottom2top[i][j])
        return ans