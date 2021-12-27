class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.pred = None
        self.first = None
        self.second = None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        if self.pred and self.pred.val > node.val:
            if not self.first:
                self.first = self.pred
            self.second = node
        self.pred = node
        self.inOrder(node.right)


class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        pred = None
        first = None
        second = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and pred.val > root.val:
                second = root
                if not first:
                    first = pred
                else:
                    break
            pred = root
            root = root.right
        first.val, second.val = second.val, first.val


class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        pred = None
        first = None
        second = None
        while root:
            if root.left:
                predsessor = root.left
                while predsessor.right and predsessor.right != root:
                    predsessor = predsessor.right
                if not predsessor.right:
                    predsessor.right = root
                    root = root.left
                else:
                    if pred and pred.val > root.val:
                        second = root
                        if not first:
                            first = pred
                    pred = root
                    predsessor.right = None
                    root = root.right
            else:
                if pred and pred.val > root.val:
                    second = root
                    if not first:
                        first = pred
                pred = root
                root = root.right

        first.val, second.val = second.val, first.val














