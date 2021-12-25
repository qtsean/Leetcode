import bisect


class Solution:
    def findRightInterval(self, intervals):
        id2interval = {}
        interval2id = {}
        for i, interval in enumerate(intervals):
            id2interval[i] = interval
            interval2id[tuple(interval)] = i
        intervals.sort()
        ans = [0 for i in range(len(intervals))]
        for interval in intervals:
            id = interval2id[tuple(interval)]
            end = interval[1]
            index = bisect.bisect_left(intervals, [end])
            if index == len(intervals):
                ans[id] = -1
            else:
                ans[id] = interval2id[tuple(intervals[index])]
        return ans