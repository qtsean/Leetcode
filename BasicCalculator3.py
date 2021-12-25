class Solution:
    def calculate(self, s):
        s = s + ")"
        return self.helper(s, 0)[0]

    def helper(self, s, index):
        number = 0
        sign = "+"
        stack = []
        while index < len(s):
            if s[index].isdigit():
                number = number * 10 + int(s[index])
            elif s[index] in "+-*/)":
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop() * number)
                elif sign == "/":
                    stack.append(int(stack.pop() / number))
                if s[index] == ")":
                    return sum(stack), index
                else:
                    number = 0
                    sign = s[index]
            elif s[index] == "(":
                number, index = self.helper(s, index+1)
            index += 1