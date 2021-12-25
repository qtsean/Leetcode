import collections


class Solution:
    def minMeetingRooms(self, intervals):
        start = collections.defaultdict(int)
        end = collections.defaultdict(int)
        timestamp = []
        for interval in intervals:
            s, e = interval[0], interval[1]
            start[s] += 1
            end[e] += 1
            timestamp.append(s)
            timestamp.append(e)
        timestamp = list(set(timestamp))
        timestamp.sort()
        cur_number = 0
        max_number = 0
        for time in timestamp:
            cur_number = cur_number + start[time] - end[time]
            max_number = max(max_number, cur_number)
        return max_number