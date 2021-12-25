class Solution:
    def longestValidParentheses(self, s):
        left = 0
        right = 0
        max_length = 0
        # left to right
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if right > left:
                left = 0
                right = 0
            if left == right:
                max_length = max(max_length, 2 * left)

        left = 0
        right = 0
        for c in s[::-1]:
            if c == ")":
                right += 1
            else:
                left += 1
            if left > right:
                left = 0
                right = 0
            if right == left:
                max_length = max(max_length, 2 * left)

        return max_length