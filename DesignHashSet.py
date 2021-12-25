import copy


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 16
        self.used = 0
        self.cache = [None for i in range(self.size)]

    def add(self, key):
        hash_key = key % self.size
        if self.cache[hash_key] is None:
            self.cache[hash_key] = ListNode(key)
            self.used += 1
        else:
            cur = self.cache[hash_key]
            if cur.val == key:
                return
            else:
                while cur.next:
                    if cur.next.val == key:
                        return
                    cur = cur.next
                cur.next = ListNode(key)
                self.used += 1
        if self.used > self.size / 2:
            self.resize()

    def remove(self, key):
        hash_key = key % self.size
        if self.cache[hash_key] is None:
            return
        cur = self.cache[hash_key]
        if cur.val == key:
            self.cache[hash_key] = cur.next
            self.used -= 1
        else:
            while cur.next and cur.next.val != key:
                cur = cur.next
            if cur.next is None:
                return
            else:
                cur.next = cur.next.next
                self.used -= 1

    def contains(self, key):
        hash_key = key % self.size
        if self.cache[hash_key] is None:
            return False
        else:
            cur = self.cache[hash_key]
            while cur and cur.val != key:
                cur = cur.next
            if not cur:
                return False
            else:
                return True

    def resize(self):
        tmp = copy.deepcopy(self.cache)
        self.size *= 2
        self.cache = [None for i in range(self.size)]
        for i in range(len(tmp)):
            if tmp[i] is not None:
                cur = tmp[i]
                while cur:
                    self.add(cur.val)
                    cur = cur.next

