class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        ans = []
        self.postTraversal(root, ans)
        return ans

    def postTraversal(self, node, ans):
        if not node:
            return
        self.postTraversal(node.left, ans)
        self.postTraversal(node.right, ans)
        ans.append(node.val)