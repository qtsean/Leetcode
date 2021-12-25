class Solution:
    def minKnightMoves(self, x, y):
        i = x
        j = y
        used = set()
        used.add((0, 0))
        queue = [(0 ,0)]
        step = 0
        while queue:
            tmp = []
            for x, y in queue:
                if x == i and y == j:
                    return step
                pos = (x + 1, y + 2)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
                pos = (x + 2, y + 1)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
                pos = (x - 1, y + 2)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
                pos = (x - 2, y + 1)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
                pos = (x + 1, y - 2)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
                pos = (x + 2, y - 1)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
                pos = (x - 1, y - 2)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
                pos = (x - 2, y - 1)
                if pos not in used:
                    tmp.append(pos)
                    used.add(pos)
            step += 1
            queue = tmp