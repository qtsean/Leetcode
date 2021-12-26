import collections


class Solution:
    def minTime(self, n: int, edges, hasApple):
        neighbors = collections.defaultdict(list)
        for l, r in edges:
            neighbors[l].append(r)
            neighbors[r].append(l)
        used = set()
        self.dfs(0, neighbors, 0, hasApple, used)
        return len(used)

    def dfs(self, node, neighbors, parent, hasApple, used):
        res = hasApple[node]
        for neighbor in neighbors[node]:
            if neighbor != parent:
                tmp = self.dfs(neighbor, neighbors, node, hasApple, used)
                if tmp:
                    used.add((node, neighbor))
                    used.add((neighbor, node))
                res = res or tmp
        return res
