import collections
class Solution:
    def makesquare(self, matchsticks):
        total_count = len(matchsticks)
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        side_length = total_length // 4
        index2length = {}
        matchsticks_left = []
        counter = collections.Counter(matchsticks)
        length_number = [[k, v] for k, v in counter.items()]
        length_number.sort()
        for index, pair in enumerate(length_number):
            index2length[index] = pair[0]
            matchsticks_left.append(pair[1])
        mem = {}
        return self.backTrack(matchsticks_left, mem, 0, total_count, side_length, 0, index2length)

    def backTrack(self, matchsticks_left, mem, count, total_count, side_length, cur_sum, index2length):
        if tuple(matchsticks_left) in mem:
            return mem[tuple(matchsticks_left)]
        if count == total_count:
            return True
        ans = False
        for index in range(len(matchsticks_left)):
            if matchsticks_left[index] == 0:
                continue
            matchsticks_left[index] -= 1
            cur_sum += index2length[index]
            if cur_sum <= side_length:
                ans = ans or self.backTrack(matchsticks_left, mem, count+1, total_count, side_length, cur_sum%side_length, index2length)
                matchsticks_left[index] += 1
                cur_sum -= index2length[index]
            else:
                matchsticks_left[index] += 1
                cur_sum -= index2length[index]
                break
        mem[tuple(matchsticks_left)] = ans
        return ans