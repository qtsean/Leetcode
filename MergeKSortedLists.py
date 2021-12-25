# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Wrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:

    def mergeKLists(self, lists):
        header = ListNode()
        cur = header
        priority_queue = []
        for head in lists:
            if head:
                priority_queue.append(Wrapper(head))
        heapq.heapify(priority_queue)
        while priority_queue:
            wrapper = heapq.heappop(priority_queue)
            node = wrapper.node
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(priority_queue, Wrapper(node.next))
        return header.next
