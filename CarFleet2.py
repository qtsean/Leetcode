class Solution:
    def getCollisionTimes(self, cars):
        ans = []
        stack = []
        for car in cars[::-1]:
            if not stack:
                ans.append(-1)
                stack.append([float('inf'), car[0], car[1]])
            else:
                while stack and (car[1] <= stack[-1][2] or (stack[-1][1] - car[0]) / (car[1] - stack[-1][2]) >= stack[-1][0]):
                    stack.pop()
                if not stack:
                    ans.append(-1)
                    stack.append([float('inf'), car[0], car[1]])
                else:
                    ans.append((stack[-1][1] - car[0]) / (car[1] - stack[-1][2]))
                    stack.append([(stack[-1][1] - car[0]) / (car[1] - stack[-1][2]), car[0], car[1]])
        return ans[::-1]