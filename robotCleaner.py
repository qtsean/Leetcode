class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set()
        obstacles = set()
        road = [[0, 0]]
        robot.clean()
        cleaned.add((0, 0))
        direction = 1
        i = 0
        j = 0
        while road:
            print(road[-1])
            while road and not self.findDirections(road[-1][0], road[-1][1], cleaned, obstacles):
                x, y = road[-1][0], road[-1][1]
                road.pop()
                i, j, direction = self.moveTo(x, y, i, j, direction, robot)
            if not road:
                return
            i, j, direction = self.moveTo(road[-1][0], road[-1][1], i, j, direction, robot)
            directions = self.findDirections(i, j, cleaned, obstacles)
            for d in directions:
                x, y, newDir = d[0], d[1], d[2]
                self.changeDirection(direction, newDir, robot)
                direction = newDir
                success = robot.move()
                if success:
                    i, j = x, y
                    road.append([i, j])
                    robot.clean()
                    cleaned.add((i, j))
                    break
                else:
                    obstacles.add((x, y))
        return

    def moveTo(self, x, y, i, j, direction, robot):
        if x == i and y == j:
            return i, j, direction
        newDir = 0
        if x == i - 1:
            newDir = 1
        elif x == i + 1:
            newDir = 3
        elif y == j + 1:
            newDir = 2
        elif y == j - 1:
            newDir = 4
        self.changeDirection(direction, newDir, robot)
        robot.move()
        return x, y, newDir

    def changeDirection(self, curDir, newDir, robot):
        if curDir - newDir == 1:
            robot.turnLeft()
        elif curDir - newDir == 2:
            robot.turnLeft()
            robot.turnLeft()
        elif curDir - newDir == 3:
            robot.turnRight()
        elif newDir - curDir == 1:
            robot.turnRight()
        elif newDir - curDir == 2:
            robot.turnLeft()
            robot.turnLeft()
        elif newDir - curDir == 3:
            robot.turnLeft()

    def findDirections(self, i, j, cleaned, obstacles):
        directions = []
        if (i - 1, j) not in cleaned and (i - 1, j) not in obstacles:
            directions.append([i - 1, j, 1])
        if (i + 1, j) not in cleaned and (i + 1, j) not in obstacles:
            directions.append([i + 1, j, 3])
        if (i, j - 1) not in cleaned and (i, j - 1) not in obstacles:
            directions.append([i, j - 1, 4])
        if (i, j + 1) not in cleaned and (i, j + 1) not in obstacles:
            directions.append([i, j + 1, 2])
        return directions

