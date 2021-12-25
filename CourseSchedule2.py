class Solution:
    def findOrder(self, numCourses, prerequisites):
        pres = {}
        depend = {}
        for i in range(numCourses):
            pres[i] = 0
            depend[i] = []
        for p in prerequisites:
            course, pre = p[0], p[1]
            pres[course] += 1
            depend[pre].append(course)
        cur_turn = []
        next_turn = []
        for course in pres:
            if pres[course] == 0:
                cur_turn.append(course)
        ans = []
        while cur_turn and len(ans) < numCourses:
            ans += cur_turn
            for course in cur_turn:
                pres.pop(course)
                for cur in depend[course]:
                    pres[cur] -= 1
                    if pres[cur] == 0:
                        next_turn.append(cur)
            cur_turn = next_turn
            next_turn = []
        if len(ans) < numCourses:
            return []
        else:
            return ans