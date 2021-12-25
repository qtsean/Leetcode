class Solution:
    def findRedundantDirectedConnection(self, edges):
        can1 = None
        can2 = None
        parent = [i for i in range(len(edges) + 1)]
        for i, edge in enumerate(edges):
            p, c = edge
            c_p = parent[c]
            if c_p != c:
                can1 = [p, c]
                can2 = [c_p, c]
                edges[i][0] = 0
                break
            else:
                parent[c] = p
        parent = [i for i in range(len(edges) + 1)]
        for edge in edges:
            p, c = edge
            p_p = self.findParent(parent, p)
            c_p = self.findParent(parent, c)
            if p_p == c_p:
                if can2 is not None:
                    return can2
                else:
                    return edge
            parent[c_p] = p_p
        return can1


    def findParent(self, parent, cur):
        if cur != parent[cur]:
            parent[cur] = self.findParent(parent, parent[cur])
        return parent[cur]
