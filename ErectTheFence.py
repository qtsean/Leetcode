class Solution:
    def outerTrees(self, trees):
        trees.sort(key=lambda x: (x[0], x[1]))
        stack1 = []
        for i in range(len(trees)):
            while len(stack1) >= 2 and self.orientaion(stack1[-2], stack1[-1], trees[i]) < 0:
                stack1.pop()
            stack1.append(tuple(trees[i]))
        stack2 = []
        for i in range(len(trees)-1, -1, -1):
            while len(stack2) >= 2 and self.orientaion(stack2[-2], stack2[-1], trees[i]) < 0:
                stack2.pop()
            stack2.append(tuple(trees[i]))
        stack1 = set(stack1)
        stack2 = set(stack2)
        stack1 = stack1.union(stack2)
        return [list(x) for x in stack1]

    def orientaion(self, x, y, z):
        return (y[0] - x[0]) * (z[1] - y[1]) - (z[0] - y[0]) * (y[1] - x[1])
