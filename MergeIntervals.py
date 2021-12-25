class Solution:
    def merge(self, intervals):
        ans = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not ans:
                ans.append(interval)
            if ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
