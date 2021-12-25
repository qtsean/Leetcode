class Solution:
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.seed(i, j, grid)
                    count += 1
        return count

    def seed(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.seed(i-1, j, grid)
        self.seed(i+1, j, grid)
        self.seed(i, j-1, grid)
        self.seed(i, j+1, grid)