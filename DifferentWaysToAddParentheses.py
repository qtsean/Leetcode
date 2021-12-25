class Solution:
    def diffWaysToCompute(self, expression):
        converted_expression = self.convert(expression)
        return self.backTrack(converted_expression)

    def compute(self, n1, n2, op):
        if op == "+":
            return n1 + n2
        if op == "-":
            return n1 - n2
        if op == "*":
            return n1 * n2

    def backTrack(self, expression):
        if len(expression) == 1:
            return expression
        res = []
        for index, c in enumerate(expression):
            if str(c) in "+-*":
                left = self.backTrack(expression[:index])
                right = self.backTrack(expression[index+1:])
                for l in left:
                    for r in right:
                        res.append(self.compute(l, r, c))
        return res

    def convert(self, expression):
        res = []
        number = 0
        for c in expression:
            if c.isdigit():
                number = number * 10 + int(c)
            else:
                res.append(number)
                number = 0
                res.append(c)
        res.append(number)
        return res
