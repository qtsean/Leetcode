class Solution:
    def scoreOfParentheses(self, s):
        factor = 1
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                factor *= 2
            else:
                factor /= 2
                if s[i-1] == "(":
                    res += factor
        return int(res)