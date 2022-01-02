import copy


def fitRectanglesIntoBoard(board, rectangles):
    holes = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                holes.append([i, j])
    mem = {}
    return dfs(0, rectangles, board, [], mem, holes)

def dfs(index, rectangles, board, usedRectangles, mem, holes):
    usedRectangles.sort()
    if tuple(usedRectangles) in mem:
        return mem[tuple(usedRectangles)]
    if index == len(rectangles):
        return True
    res = False
    cur_rectangle = rectangles[index]
    for i in range(len(board)):
        for j in range(len(board[0])):

            x1, y1 = i, j
            x2, y2 = i+cur_rectangle[0], j+cur_rectangle[1]
            tmp = [x1, y1, x2, y2]
            if checkPositionValid(i, j, usedRectangles, holes, tmp, board):
                new_rectangles = copy.deepcopy(usedRectangles)
                new_rectangles.append(tuple(tmp))
                res = res or dfs(index+1, rectangles, board, new_rectangles, mem, holes)

            x2, y2 = i+cur_rectangle[1], j+cur_rectangle[0]
            tmp = [x1, y1, x2, y2]
            if checkPositionValid(i, j, usedRectangles, holes, tmp, board):
                new_rectangles = copy.deepcopy(usedRectangles)
                new_rectangles.append(tuple(tmp))
                res = res or dfs(index + 1, rectangles, board, new_rectangles, mem, holes)

    mem[tuple(usedRectangles)] = res
    print(mem)
    return res




def checkPositionValid(i, j, usedRectangles, holes, cur_rectangle, board):
    if cur_rectangle[0] < 0 or cur_rectangle[1] < 0 or cur_rectangle[2] > len(board) or cur_rectangle[3] > len(board[0]):
        return False
    for hole in holes:
        if not checkHoleNotInRec(hole, [cur_rectangle[0], cur_rectangle[1]], [cur_rectangle[2], cur_rectangle[3]]):
            return False
    for rec in usedRectangles:
        if not checkRecOverLap(rec[0], rec[1], rec[2], rec[3], cur_rectangle[0], cur_rectangle[1], cur_rectangle[2], cur_rectangle[3]):
            return False
    return True

def checkRecOverLap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if ax1 >= bx2 or ax2 <= bx1 or ay1 >= by2 or ay2 <= by1:
        return True
    else:
        return False

def checkHoleNotInRec(hole, left_up, right_bottom):
    x, y = hole
    up = left_up[0]
    left = left_up[1]
    right = right_bottom[1]
    bottom = right_bottom[0]
    if left <= y < right and up <= x < bottom:
        return False
    else:
        return True


begin_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0]
]
rectanglesList = [
    [3, 5],
    [1, 5],
    [1, 2],
    [1, 4],
    [2, 3],
    [1, 2],
    [1, 1]
]

print(fitRectanglesIntoBoard(begin_board, rectanglesList))
