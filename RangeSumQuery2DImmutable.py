class NumMatrix:

    def __init__(self, matrix):
        self.mat = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    self.mat[i][j] = matrix[i][j]
                elif i == 0:
                    self.mat[i][j] = self.mat[i][j-1] + matrix[i][j]
                elif j == 0:
                    self.mat[i][j] = self.mat[i-1][j] + matrix[i][j]
                else:
                    self.mat[i][j] = self.mat[i-1][j] + self.mat[i][j-1] - self.mat[i-1][j-1] + matrix[i][j]



    def sumRegion(self, row1, col1, row2, col2):
        if row1 == 0 and col1 == 0:
            return self.mat[row2][col2]
        elif row1 == 0:
            return self.mat[row2][col2] - self.mat[row2][col1-1]
        elif col1 == 0:
            return self.mat[row2][col2] - self.mat[row1-1][col2]
        else:
            return self.mat[row2][col2] - self.mat[row1-1][col2] - self.mat[row2][col1-1] + self.mat[row1-1][col1-1]