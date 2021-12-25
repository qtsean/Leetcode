class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        self.valid = True
        self.unionFind(edges, n)
        return self.valid

    def unionFind(self, edges, n):
        parent = [i for i in range(n)]
        for edge in edges:
            l, r = edge
            l_parent = self.findParent(parent, l)
            r_parent = self.findParent(parent, r)
            if l_parent == r_parent:
                self.valid = False
            parent[r_parent] = l_parent

    def findParent(self, parent, cur):
        if cur != parent[cur]:
            parent[cur] = self.findParent(parent, parent[cur])
        return parent[cur]