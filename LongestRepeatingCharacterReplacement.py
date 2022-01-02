import collections


class Solution:
    def characterReplacement(self, s, k):
        ans = 0
        count = collections.defaultdict(list)
        l = r = 0
        max_freq = 0
        while r < len(s):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            if r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            r += 1
        return r - l + 1
