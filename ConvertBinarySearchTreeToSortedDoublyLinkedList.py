class Solution:
    def treeToDoublyList(self, root):
        head, tail = self.helper(root)
        head.left = tail
        tail.right = head
        return head
    def helper(self, node):
        if not node:
            return None, None
        left_head, left_tail = self.helper(node.left)
        right_head, right_tail = self.helper(node.right)
        if left_tail:
            node.left = left_tail
            left_tail.right = node
        if right_head:
            node.right = right_head
            right_head.left = node
        l = left_head if left_head else node
        r = right_tail if right_tail else node
        return l, r