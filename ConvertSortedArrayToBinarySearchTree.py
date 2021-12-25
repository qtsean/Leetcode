# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        left = 0
        right = len(nums) - 1
        return self.construct(left, right, nums)

    def construct(self, left, right, nums):
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.construct(left, mid-1, nums)
        node.right = self.construct(mid+1, right, nums)
