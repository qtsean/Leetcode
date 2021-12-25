class Solution:
    def shortestBridge(self, grid):
        island1 = None
        island2 = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tmp = []
                    self.seed(i, j, grid, tmp)
                    if island1 is None:
                        island1 = tmp
                    else:
                        island2 = tmp
        visited = set()
        for pos in island1:
            visited.add(pos)
        queue = island1
        target = set()
        for pos in island2:
            target.add(pos)
        step = 0
        while queue:
            tmp = []
            for i, j in queue:
                if (i, j) in target:
                    return step - 1
                if self.checkValid(i-1, j, visited, grid):
                    visited.add((i-1, j))
                    tmp.append((i-1, j))
                if self.checkValid(i+1, j, visited, grid):
                    visited.add((i+1, j))
                    tmp.append((i+1, j))
                if self.checkValid(i, j-1, visited, grid):
                    visited.add((i, j-1))
                    tmp.append((i, j-1))
                if self.checkValid(i, j+1, visited, grid):
                    visited.add((i, j+1))
                    tmp.append((i, j+1))
            step += 1
            queue = tmp


    def checkValid(self, i, j, visited, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in visited:
            return True
        return False


    def seed(self, i, j, grid, tmp):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 2
        tmp.append((i, j))
        self.seed(i-1, j, grid, tmp)
        self.seed(i+1, j, grid, tmp)
        self.seed(i, j-1, grid, tmp)
        self.seed(i, j+1, grid, tmp)