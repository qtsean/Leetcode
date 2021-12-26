import copy


class Solution:
    def minFlips(self, mat):
        used = set()
        target_mat = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        target = self.toTuple(target_mat)
        used.add(self.toTuple(mat))
        queue = [mat]
        step = 0
        while queue:
            tmp = []
            for q in queue:
                if self.toTuple(q) == target:
                    return step
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        new_mat = copy.deepcopy(q)
                        self.flip(new_mat, i, j)
                        if self.toTuple(new_mat) not in used:
                            used.add(self.toTuple(new_mat))
                            tmp.append(new_mat)
            queue = tmp
            step += 1
        return -1


    def flip(self, mat, i, j):
        mat[i][j] ^= 1
        if i-1 >= 0:
            mat[i-1][j] ^= 1
        if i+1 < len(mat):
            mat[i+1][j] ^= 1
        if j-1 >= 0:
            mat[i][j-1] ^= 1
        if j+1 < len(mat[0]):
            mat[i][j+1] ^= 1

    def toTuple(self, mat):
        tmp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                tmp.append(mat[i][j])
        return tuple(tmp)


