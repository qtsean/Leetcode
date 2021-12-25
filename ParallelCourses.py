class Solution:
    def minimumSemesters(self, n, relations):
        pres = {}
        depends = {}
        for i in range(1, n+1):
            pres[i] = 0
            depends[i] = []
        for p, nxt in relations:
            pres[nxt] += 1
            depends[p].append(nxt)
        cur_turn = []
        for key in pres.keys():
            if pres[key] == 0:
                cur_turn.append(key)
        taken = 0
        semesters = 0
        while cur_turn and taken < n:
            taken += len(cur_turn)
            next_turn = []
            for course in cur_turn:
                pres.pop(course)
                for cur in depends[course]:
                    pres[cur] -= 1
                    if pres[cur] == 0:
                        next_turn.append(cur)
            semesters += 1
            cur_turn = next_turn
        if taken == n:
            return semesters
        else:
            return -1
