class Solution:
    def multiply(self, mat1, mat2):
        row1 = len(mat1)
        col1 = len(mat1[0])
        row2 = len(mat2)
        col2 = len(mat2[0])
        mat = [[0 for j in range(col2)] for i in range(row1)]
        new_mat1 = []
        new_mat2 = []
        for i in range(row1):
            for j in range(col1):
                if mat1[i][j] != 0:
                    new_mat1.append([i, j, mat1[i][j]])
        for i in range(row2):
            for j in range(col2):
                if mat2[i][j] != 0:
                    new_mat2.append([i, j, mat2[i][j]])
        for pair1 in new_mat1:
            i1, j1, num1 = pair1
            for pair2 in new_mat2:
                i2, j2, num2 = pair2
                if j1 == i2:
                    mat[i1][j2] += num1 * num2
        return mat