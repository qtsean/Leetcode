from filecmp import cmp


class Solution:
    def combinationSum2(self, candidates, target):
        ans = set()
        candidates.sort()
        mem = {}
        self.backTrack(candidates, target, [], 0, ans, 0, mem)
        return [list(x) for x in ans]

    def backTrack(self, candidates, target, tmp, val, ans, index, mem):
        if tuple([index, tuple(tmp)]) in mem:
            return mem[tuple([index, tuple(tmp)])]
        if index >= len(candidates):
            return
        if val == target:
            ans.add(tuple(tmp))
            return
        if val > target:
            return
        self.backTrack(candidates, target, tmp + [candidates[index]], val + candidates[index], ans, index + 1, mem)
        self.backTrack(candidates, target, tmp, val, ans, index + 1, mem)
        mem[tuple([index, tuple(tmp)])] = True
