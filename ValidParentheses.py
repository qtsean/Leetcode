class Solution:
    def isValid(self, s: str):
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if c == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif c == "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    if stack and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
