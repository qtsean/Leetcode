# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        size = self.countSize(head)
        self.ptr = head
        return self.construct(0, size-1)


    def construct(self, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        left_tree = self.construct(left, mid-1)
        node = TreeNode(self.ptr.val)
        self.ptr = self.ptr.next
        node.left = left_tree
        node.right = self.construct(mid+1, right)
        return node


    def countSize(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
