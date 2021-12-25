import collections


class Solution:
    def canPartitionKSubsets(self, nums, k):
        total_count = len(nums)
        total_value = sum(nums)
        if total_value % k != 0:
            return False
        each_value = total_value // k
        number_left = []
        index2value = {}
        counter = collections.Counter(nums)
        mem = {}
        value_number = [[k, v] for k, v in counter.items()]
        value_number.sort(reverse=True)
        for index, pair in enumerate(value_number):
            index2value[index] = pair[0]
            number_left.append(pair[1])
        return self.backTrack(0, total_count, mem, number_left, 0, each_value, index2value)

    def backTrack(self, count, total_count, mem, number_left, cur_sum, each_value, index2value):
        if tuple(number_left) in mem:
            return mem[tuple(number_left)]
        if count == total_count:
            return True
        ans = False
        for i in range(len(number_left)):
            if number_left[i] == 0:
                continue
            number_left[i] -= 1
            cur_sum += index2value[i]
            if cur_sum <= each_value:
                ans = ans or self.backTrack(count+1, total_count, mem, number_left, cur_sum % each_value, each_value, index2value)
                if ans:
                    break
            number_left[i] += 1
            cur_sum -= index2value[i]
        mem[tuple(number_left)] = ans
        return ans