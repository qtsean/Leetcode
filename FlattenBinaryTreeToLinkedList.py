# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, node):
        if not node:
            return None, None
        if not node.left and not node.right:
            return node, node
        left_head, left_tail = self.helper(node.left)
        right_head, right_tail = self.helper(node.right)
        node.left = None
        if left_head and right_head:
            node.right = left_head
            left_tail.right = right_head
            return node, right_tail
        elif left_head and not right_head:
            node.right = left_head
            return node, left_tail
        elif not left_head and right_head:
            node.right = right_head
            return node, right_tail
        else:
            return node, node
