def read4(buf):
    return 1

class Solution:

    def __init__(self):
        self.cache = [None, None, None, None]
        self.file_has_left = True
        self.cache_index = 0
        self.cache_valid = 0

    def read(self, buf, n):
        count = 0
        while count < n and self.file_has_left and self.cache_index == self.cache_valid:
            self.cache_valid = read4(self.cache)
            self.cache_index = 0
            if self.cache_valid < 4:
                self.file_has_left = False
            while self.cache_index < self.cache_valid and count < n:
                buf[count] = self.cache[self.cache_index]
                count += 1
                self.cache_index += 1
            if count == n:
                return n
            else:
                if self.file_has_left:
                    continue
                else:
                    break
        return count
