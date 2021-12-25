class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        self.ans = True
        self.dfs(root, float("-inf"), float("inf"))
        return self.ans

    def dfs(self, node, min_val, max_val):
        if not node:
            return
        if node.val <= min_val or node.val >= max_val:
            self.ans = False
            return
        self.dfs(node.left, min_val, node.val)
        self.dfs(node.right, node.val, max_val)
