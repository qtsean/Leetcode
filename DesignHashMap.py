import copy


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 16
        self.used = 0
        self.cache = [ListNode("#", "#") for i in range(self.size)]

    def put(self, key, value) -> None:
        hash_key = key % self.size
        cur = self.cache[hash_key]
        while cur.next and cur.next.key != key:
            cur = cur.next
        if cur.next is None:
            cur.next = ListNode(key, value)
            self.used += 1
        else:
            cur.next.val = value
        if self.used > self.size / 2:
            self.resize()

    def get(self, key):
        hash_key = key % self.size
        cur = self.cache[hash_key]
        while cur and cur.key != key:
            cur = cur.next
        if not cur:
            return -1
        else:
            return cur.val

    def remove(self, key):
        hash_key = key % self.size
        cur = self.cache[hash_key]
        while cur.next and cur.next.key != key:
            cur = cur.next
        if not cur.next:
            return
        else:
            cur.next = cur.next.next
            self.used -= 1

    def resize(self):
        tmp = copy.deepcopy(self.cache)
        self.size *= 2
        self.cache = [ListNode("#", "#") for i in range(self.size)]
        for i in range(len(tmp)):
            if tmp[i]:
                cur = tmp[i]
                while cur:
                    self.put(cur.key, cur.val)
                    cur = cur.next
