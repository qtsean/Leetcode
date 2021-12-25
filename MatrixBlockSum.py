class Solution:
    def matrixBlockSum(self, mat, k):
        self.buildPrefixMatrix(mat)
        new_mat = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                i1 = max(0, i-k)
                j1 = max(0, j-k)
                i2 = min(len(mat)-1, i+k)
                j2 = min(len(mat[0])-1, j+k)
                new_mat[i][j] = self.getSum(i1, j1, i2, j2, mat)
        return new_mat

    def getSum(self, i1, j1, i2, j2, mat):
        if i1 == 0 and j1 == 0:
            return mat[i2][j2]
        elif i1 == 0 and j1 != 0:
            return mat[i2][j2] - mat[i2][j1-1]
        elif i1 != 0 and j1 == 0:
            return mat[i2][j2] - mat[i1-1][j2]
        else:
            return mat[i2][j2] - mat[i2][j1-1] - mat[i1-1][j2] + mat[i1-1][j1-1]

    def buildPrefixMatrix(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0 and j == 0:
                    mat[i][j] = mat[i][j]
                elif i == 0 and j != 0:
                    mat[i][j] = mat[i][j] + mat[i][j-1]
                elif i != 0 and j == 0:
                    mat[i][j] = mat[i][j] + mat[i-1][j]
                else:
                    mat[i][j] = mat[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]