import collections


class LRUCache:

    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        return -1

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

