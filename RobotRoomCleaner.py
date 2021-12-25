# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        i = 0
        j = 0
        dir = 0
        cleaned = set()
        obstacles = set()
        robot.clean()
        cleaned.add((0, 0))
        path = [[i, j]]
        while path:
            while path and not self.findDirection(cleaned, obstacles, path[-1][0], path[-1][1]):
                x, y = path.pop()
                i, j, dir = self.move(x, y, i, j, dir, robot)
            if not path:
                return
            i, j, dir = self.move(path[-1][0], path[-1][1], i, j, dir, robot)
            for position in self.findDirection(cleaned, obstacles, i, j):
                x, y, new_dir = position
                self.changeDirection(new_dir, dir, robot)
                dir = new_dir
                if robot.move():
                    robot.clean()
                    i = x
                    j = y
                    cleaned.add((i, j))
                    path.append([i, j])
                    break
                else:
                    obstacles.add((x, y))





    def findDirection(self, cleaned, obstacles, i, j):
        res = []
        if (i-1, j) not in cleaned and (i-1, j) not in obstacles:
            res.append([i-1, j, 0])
        if (i+1, j) not in cleaned and (i+1, j) not in obstacles:
            res.append([i+1, j, 2])
        if (i, j-1) not in cleaned and (i, j-1) not in obstacles:
            res.append([i, j-1, 3])
        if (i, j+1) not in cleaned and (i, j+1) not in obstacles:
            res.append([i, j+1, 1])
        return res

    def move(self, x, y, i, j, cur_dir, robot):
        if x == i and y == j:
            return i, j, cur_dir
        new_dir = None
        if x == i - 1:
            new_dir = 0
        elif x == i + 1:
            new_dir = 2
        elif y == j + 1:
            new_dir = 1
        elif y == j - 1:
            new_dir = 3
        self.changeDirection(new_dir, cur_dir, robot)
        robot.move()
        return x, y, new_dir


    def changeDirection(self, new_dir, cur_dir, robot):
        if new_dir - cur_dir == 1:
            robot.turnRight()
        elif new_dir - cur_dir == 2:
            robot.turnRight()
            robot.turnRight()
        elif new_dir - cur_dir == 3:
            robot.turnLeft()
        elif cur_dir - new_dir == 1:
            robot.turnLeft()
        elif cur_dir - new_dir == 2:
            robot.turnLeft()
            robot.turnLeft()
        elif cur_dir - new_dir == 3:
            robot.turnRight()



































