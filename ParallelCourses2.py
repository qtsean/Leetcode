import collections
import copy
from functools import lru_cache
from itertools import combinations


class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        mask = 0
        for i in range(n):
            mask += 1 << i
        pres = [0 for i in range(n)]
        depends = collections.defaultdict(list)
        for pre, nxt in relations:
            pres[nxt-1] += 1
            depends[pre-1].append(nxt-1)

        @lru_cache(None)
        def dfs(msk):
            if msk == 0:
                return 0
            take = []
            for index in range(len(pres)):
                if pres[index] == 0 and msk&(1 << index):
                    take.append(index)
            res = float("inf")
            for c in combinations(take, min(k, len(take))):
                m = msk
                for course in c:
                    m ^= (1 << course)
                    for next_course in depends[course]:
                        pres[next_course] -= 1
                res = min(res, 1+dfs(m,))
                for course in c:
                    for next_course in depends[course]:
                        pres[next_course] += 1
            return res

        return dfs(mask)