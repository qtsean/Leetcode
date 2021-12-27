class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def correctBinaryTree(self, root):
        depth = set()
        self.dfs(root, depth)
        return root
    def dfs(self, node, depth):
        if not node:
            return False
        depth.add(node)
        if node.right in depth:
            return True
        if self.dfs(node.right, depth):
            node.right = None
        if self.dfs(node.left, depth):
            node.left = None
        return False