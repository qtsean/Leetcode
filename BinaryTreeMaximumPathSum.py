class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')
        self.traverse(root)
        return self.ans

    def traverse(self, node):
        if not node:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        self.ans = max(self.ans, node.val + max(0, left) + max(0, right))
        return max(left, right, 0) + node.val
