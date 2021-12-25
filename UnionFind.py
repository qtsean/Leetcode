class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(n+1)]
        for edge in edges:
            l = edge[0]
            r = edge[1]
            p_l = self.findParent(parent, l)
            p_r = self.findParent(parent, r)
            if p_l == p_r:
                return edge
            else:
                parent[r] = p_l
        return

    def findParent(self, parent, cur):
        if cur != parent[cur]:
            parent[cur] = self.findParent(parent, parent[cur])
        return parent[cur]