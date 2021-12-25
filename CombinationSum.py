class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        self.dfs(0, target, 0, candidates, [],  ans)
        return ans

    def dfs(self, cur_sum, target, index, candidates, cur_num, ans):
        if cur_sum == target:
            ans.append(cur_num)
            return
        if index == len(candidates):
            return
        tmp = []
        while cur_sum <= target:
            self.dfs(cur_sum, target, index+1, candidates, cur_num + tmp, ans)
            cur_sum += candidates[index]
            tmp.append(candidates[index])