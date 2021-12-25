import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        prefix_matrix = self.buildPrefixMatrix(matrix)
        ans = 0
        for i1 in range(len(matrix)):
            for i2 in range(i1, len(matrix)):
                dic = collections.defaultdict(int)
                dic[0] = 1
                for j in range(len(matrix[0])):
                    s = self.getSum(prefix_matrix, i1, 0, i2, j)
                    ans += dic[s - target]
                    dic[s] += 1
        return ans

    def getSum(self, matrix, i1, j1, i2, j2):
        if i1 == 0 and j1 == 0:
            return matrix[i2][j2]
        elif i1 != 0 and j1 == 0:
            return matrix[i2][j2] - matrix[i1-1][j2]
        elif i1 == 0 and j1 != 0:
            return matrix[i2][j2] - matrix[i2][j1-1]
        else:
            return matrix[i2][j2] - matrix[i1-1][j2] - matrix[i2][j1-1] + matrix[i1-1][j1-1]


    def buildPrefixMatrix(self, matrix):
        mat = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    mat[i][j] = matrix[i][j]
                elif i == 0 and j != 0:
                    mat[i][j] = mat[i][j-1] + matrix[i][j]
                elif i != 0 and j == 0:
                    mat[i][j] = mat[i-1][j] + matrix[i][j]
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1] + matrix[i][j]
        return mat
