class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        return self.construct(root1, root2)

    def construct(self, node1, node2):
        if node1 is None and node2 is None:
            return None
        elif node1 is not None and node2 is None:
            node = TreeNode(node1.val)
            node.left = self.construct(node1.left, node2)
            node.right = self.construct(node1.right, node2)
        elif node2 is not None and node1 is None:
            node = TreeNode(node2.val)
            node.left = self.construct(node1, node2.left)
            node.right = self.construct(node1, node2.right)
        else:
            node = TreeNode(node1.val + node2.val)
            node.left = self.construct(node1.left, node2.left)
            node.right = self.construct(node1.right, node2.right)
        return node
