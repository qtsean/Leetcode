class Solution:
    def nearestValidPoint(self, x, y, points):
        ans = -1
        dist = float('inf')
        for index, (i, j) in enumerate(points):
            if i == x or j == y:
                if abs(i-x) + abs(j-y) < dist:
                    dist = abs(i-x) + abs(j-y)
                    ans = index
        return ans