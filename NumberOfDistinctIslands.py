class Solution:
    def numDistinctIslands(self, grid):
        count = 0
        shapes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tmp = []
                    self.seed(i, j, grid, tmp)
                    self.moveShape(tmp)
                    if not self.checkInShapes(shapes, tmp):
                        shapes.append(tmp)
                        count += 1
        return count

    def seed(self, i, j, grid, tmp):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 2
        tmp.append([i, j])
        self.seed(i-1, j, grid, tmp)
        self.seed(i+1, j, grid, tmp)
        self.seed(i, j-1, grid, tmp)
        self.seed(i, j+1, grid, tmp)

    def checkInShapes(self,shapes, tmp):
        for shape in shapes:
            if self.isSame(shape, tmp):
                return True
        return False
        
    def isSame(self, shape, tmp):
        if len(shape) != len(tmp):
            return False
        for i in range(len(tmp)):
            if tmp[i][0] != shape[i][0] or tmp[i][1] != shape[i][1]:
                return False
        return True

    def moveShape(self, tmp):
        x = tmp[0][0]
        y = tmp[0][1]
        for i in range(len(tmp)):
            tmp[i][0] -= x
            tmp[i][1] -= y


