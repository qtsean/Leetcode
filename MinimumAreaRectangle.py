import collections


class Solution:
    def minAreaRect(self, points):
        ans = float('inf')
        points_set = set([tuple(point) for point in points])
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                i1, j1 = points[i]
                i2, j2 = points[j]
                if i1 == i2 or j1 == j2:
                    continue
                if (i1, j2) in points_set and (i2, j1) in points_set:
                    ans = min(ans, abs(i1-i2) * abs(j1-j2))
        return ans if ans < float('inf') else 0
