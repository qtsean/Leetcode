import collections


class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        # Check no cycles
        # Check no multiple trees
        # Check root exists
        children = {}
        parent = {}
        for i in range(n):
            children[i] = []
            parent[i] = []
        for i, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l != -1:
                children[i].append(l)
                parent[l].append(i)
            if r != -1:
                children[i].append(r)
                parent[r].append(i)
        root = None
        for key in parent.keys():
            if len(parent[key]) == 0:
                root = key
        if root is None:
            return False
        used = set()
        return self.dfs(root, children, used) and len(used) == n

    def dfs(self, node, children, used):
        if node in used:
            return False
        ans = True
        used.add(node)
        for c in children[node]:
            ans = ans and self.dfs(c, children, used)
        return ans