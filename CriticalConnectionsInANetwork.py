class Solution:
    def criticalConnections(self, n, connections):
        depth = {}
        neighbors = {}
        is_critical = set()
        for i in range(n):
            neighbors[i] = []
        for left, right in connections:
            is_critical.add((left, right))
            neighbors[left].append(right)
            neighbors[right].append(left)
        ans = []
        self.dfs(depth, 0, 1, is_critical, 0, neighbors)
        for connection in is_critical:
            ans.append(list(connection))
        return ans

    def dfs(self, depth, node, cur_depth, is_critical, parent, neighbors):
        if node in depth:
            return depth[node]
        depth[node] = cur_depth
        res = cur_depth
        for neighbor in neighbors[node]:
            if neighbor != parent:
                tmp = self.dfs(depth, neighbor, cur_depth+1, is_critical, node, neighbors)
                if tmp <= cur_depth:
                    if (node, neighbor) in is_critical:
                        is_critical.remove((node, neighbor))
                    if (neighbor, node) in is_critical:
                        is_critical.remove((neighbor, node))
                res = min(res, tmp)
        return res
