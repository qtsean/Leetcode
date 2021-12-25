class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        ans = []
        for i, c in enumerate(s):
            if c == "(":
                ans.append("")
                stack.append(i)
            elif c == ")":
                if stack:
                    j = stack.pop()
                    ans[j] = "("
                    ans.append(")")
                else:
                    ans.append("")
            else:
                ans.append(c)
        return "".join(ans)
