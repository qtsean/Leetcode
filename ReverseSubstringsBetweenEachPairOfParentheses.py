class Solution:
    def reverseParentheses(self, s):
        stack = [""]
        for c in s:
            if c == "(":
                stack.append("")
            elif c == ")":
                cur = stack.pop()
                stack[-1] += cur[::-1]
            else:
                stack[-1] += c
        return "".join(stack)


class Solution:
    def reverseParentheses(self, s):
        stack = []
        pair = {}
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        ans = []
        index = 0
        d = 1
        while index < len(s):
            if s[index] in "()":
                index = pair[index]
                d *= -1
            else:
                ans.append(s[index])
            index += d
        return "".join(ans)


