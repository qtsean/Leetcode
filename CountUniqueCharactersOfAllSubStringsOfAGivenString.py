import string


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        dic = {c: [-1, -1] for c in string.ascii_uppercase}
        for i, c in enumerate(s):
            j, k = dic[c]
            ans += (i - k) * (k - j)
            dic[c] = [k, i]
        for c in dic.keys():
            j, k = dic[c]
            ans += (len(s) - k) * (k - j)
        return ans