class Solution:
    def spiralOrder(self, matrix):
        up_bound = 0
        down_bound = len(matrix) - 1
        left_bound = 0
        right_bound = len(matrix[0]) - 1
        ans = []
        direction = "right"
        total_length = len(matrix) * len(matrix[0])
        cur_row = 0
        cur_col = 0
        while len(ans) < total_length:
            if direction == "right":
                for i in range(cur_col, right_bound + 1):
                    ans.append(matrix[cur_row][i])
                up_bound += 1
                cur_col = right_bound
                direction = "down"
                cur_row += 1
            elif direction == "down":
                for i in range(cur_row, down_bound + 1):
                    ans.append(matrix[i][cur_col])
                right_bound -= 1
                cur_row = down_bound
                direction = "left"
                cur_col -= 1
            elif direction == "left":
                for i in range(cur_col, left_bound - 1, -1):
                    ans.append(matrix[cur_row][i])
                down_bound -= 1
                cur_col = left_bound
                direction = "up"
                cur_row -= 1
            else:
                for i in range(cur_row, up_bound - 1, -1):
                    ans.append(matrix[i][cur_col])
                left_bound += 1
                cur_row = up_bound
                direction = "right"
                cur_col += 1
        return ans
