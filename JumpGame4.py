import collections


class Solution:
    def minJumps(self, arr):
        neighbors = collections.defaultdict(list)
        for i, n in enumerate(arr):
            neighbors[n].append(i)
        visited = set()
        visited.add(0)
        end = len(arr)- 1
        queue = [0]
        step = 0
        while queue:
            tmp = []
            for q in queue:
                if q == end:
                    return step
                if q-1 >= 0 and q-1 not in visited:
                    visited.add(q-1)
                    tmp.append(q-1)
                if q+1 < len(arr) and q+1 not in visited:
                    visited.add(q+1)
                    tmp.append(q+1)
                for neighbor in neighbors[arr[q]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        tmp.append(neighbor)
                neighbors[arr[q]] = []
            queue = tmp
            step += 1