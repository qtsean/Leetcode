class Solution:
    def numDistinctIslands2(self, grid):
        shapes = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tmp = []
                    self.seed(i, j, grid, tmp)
                    tmp = self.normalize(tmp)
                    if self.checkValid(shapes, tmp):
                        count += 1
                        shapes.add(tuple(tmp))
        return count

    def seed(self, i, j, grid, path):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 2
        path.append((i, j))
        self.seed(i-1, j, grid, path)
        self.seed(i+1, j, grid, path)
        self.seed(i, j-1, grid, path)
        self.seed(i, j+1, grid, path)

    def normalize(self, tmp):
        tmp.sort()
        return [(x-tmp[0][0], y-tmp[0][1]) for x, y in tmp]

    def checkValidRotate(self, shapes, path):
        for i in range(3):
            path = [(y, -x) for x, y in path]
            path = self.normalize(path)
            if tuple(path) in shapes:
                return False
        return True

    def checkValid(self, shapes, path):
        if tuple(path) in shapes or not self.checkValidRotate(shapes, path):
            return False
        hon_path = [(-x, y) for x, y in path]
        hon_path = self.normalize(hon_path)
        if tuple(hon_path) in shapes or not self.checkValidRotate(shapes, hon_path):
            return False
        ver_path = [(x, -y) for x, y in path]
        ver_path = self.normalize(ver_path)
        if tuple(ver_path) in shapes or not self.checkValidRotate(shapes, ver_path):
            return False
        return True

