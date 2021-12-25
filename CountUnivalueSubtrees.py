class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countUnivalSubtrees(self, root):
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            self.ans += 1
            return root.val
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == False or (left != None and left != root.val) or right == False or (None != True and right != root.val):
            return False
        self.ans += 1
        return root.val