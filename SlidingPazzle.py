import copy


class Solution:
    def slidingPuzzle(self, board):
        target = [[1, 2, 3], [4, 5, 6]]
        used = set()
        step = 0
        zero_x = None
        zero_y = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    zero_x = i
                    zero_y = j
        start = [[board, zero_x, zero_y]]
        used.add(self.toString(board))
        while start:
            tmp = []
            for cur in start:
                cur_board, cur_x, cur_y = cur
                if self.toString(cur_board) == self.toString(target):
                    return step
                if cur_x - 1 >= 0:
                    new_board = copy.deepcopy(cur_board)
                    new_board[cur_x][cur_y], new_board[cur_x-1][cur_y] = new_board[cur_x-1][cur_y], new_board[cur_x][cur_y]
                    if self.toString(new_board) not in used:
                        tmp.append([new_board, cur_x-1, cur_y])
                        used.add(self.toString(new_board))
                if cur_x + 1 < len(board):
                    new_board = copy.deepcopy(cur_board)
                    new_board[cur_x][cur_y], new_board[cur_x+1][cur_y] = new_board[cur_x+1][cur_y], new_board[cur_x][cur_y]
                    if self.toString(new_board) not in used:
                        tmp.append([new_board, cur_x+1, cur_y])
                        used.add(self.toString(new_board))

                if cur_y - 1 >= 0:
                    new_board = copy.deepcopy(cur_board)
                    new_board[cur_x][cur_y], new_board[cur_x][cur_y-1] = new_board[cur_x][cur_y-1], \
                                                                           new_board[cur_x][cur_y]
                    if self.toString(new_board) not in used:
                        tmp.append([new_board, cur_x, cur_y-1])
                        used.add(self.toString(new_board))

                if cur_y + 1 < len(board[0]):
                    new_board = copy.deepcopy(cur_board)
                    new_board[cur_x][cur_y], new_board[cur_x][cur_y+1] = new_board[cur_x][cur_y+1], \
                                                                           new_board[cur_x][cur_y]
                    if self.toString(new_board) not in used:
                        tmp.append([new_board, cur_x, cur_y+1])
                        used.add(self.toString(new_board))
            step += 1
            start = tmp
        return -1
    def toString(self, board):
        tmp = []
        for row in board:
            tmp += [str(x) for x in row]
        return "".join(tmp)