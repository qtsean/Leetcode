class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        next_start = root
        cur = next_start
        while next_start:
            cur = next_start
            next_start = None
            prev = None
            while cur:
                if not next_start:
                    if cur.left:
                        next_start = cur.left
                    elif cur.right:
                        next_start = cur.right
                if not prev and cur.left:
                    prev = cur.left
                elif prev and cur.left:
                    prev.next = cur.left
                    prev = cur.left
                if not prev and cur.right:
                    prev = cur.right
                elif prev and cur.right:
                    prev.next = cur.right
                    prev = cur.right
                cur = cur.next
        return root
    