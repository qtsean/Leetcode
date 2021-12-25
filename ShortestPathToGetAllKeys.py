class Solution:
    def shortestPathAllKeys(self, grid):
        x = None
        y = None
        mask = 0
        lock2number = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}
        key2number = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
        total_mask = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    x = i
                    y = j
                if grid[i][j].islower():
                    number = key2number[grid[i][j]]
                    total_mask = total_mask | (1 << number)

        used = set()
        used.add((x, y, mask))
        queue = [[x, y, mask]]
        step = 0
        while queue:
            tmp = []
            for q in queue:
                i, j, mask = q
                if mask == total_mask:
                    return step
                if self.checkValid(i-1, j, grid, mask, lock2number):
                    new_mask = mask
                    if grid[i-1][j].islower():
                        number = key2number[grid[i-1][j]]
                        new_mask = mask | (1 << number)
                    if (i-1, j, new_mask) not in used:
                        tmp.append([i-1, j, new_mask])
                        used.add((i-1, j, new_mask))
                if self.checkValid(i+1, j, grid, mask, lock2number):
                    new_mask = mask
                    if grid[i+1][j].islower():
                        number = key2number[grid[i+1][j]]
                        new_mask = mask | (1 << number)
                    if (i+1, j, new_mask) not in used:
                        tmp.append([i+1, j, new_mask])
                        used.add((i+1, j, new_mask))
                if self.checkValid(i, j-1, grid, mask, lock2number):
                    new_mask = mask
                    if grid[i][j-1].islower():
                        number = key2number[grid[i][j-1]]
                        new_mask = mask | (1 << number)
                    if (i, j-1, new_mask) not in used:
                        tmp.append([i, j-1, new_mask])
                        used.add((i, j-1, new_mask))
                if self.checkValid(i, j+1, grid, mask, lock2number):
                    new_mask = mask
                    if grid[i][j+1].islower():
                        number = key2number[grid[i][j+1]]
                        new_mask = mask | (1 << number)
                    if (i, j+1, new_mask) not in used:
                        tmp.append([i, j+1, new_mask])
                        used.add((i, j+1, new_mask))
            queue = tmp
            step += 1
        return -1
    def checkValid(self, i, j, grid, mask, lock2number):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != "#":
            if grid[i][j].isupper():
                number = lock2number[grid[i][j]]
                if mask == mask | (1 << number):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
