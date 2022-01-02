import collections
import heapq


class Solution:
    def medianSlidingWindow(self, nums, k):
        left = []
        right = []
        balance = 0
        ans = []
        count = collections.defaultdict(int)
        for i in range(len(nums)):
            if not left or nums[i] < -left[0]:
                heapq.heappush(left, -nums[i])
                balance += 1
            else:
                heapq.heappush(right, nums[i])
                balance -= 1
            if i >= k:
                out_num = nums[i-k]
                count[out_num] += 1
                if out_num <= -left[0]:
                    balance -= 1
                else:
                    balance += 1
            balance = self.adjustBalance(left, right, balance, count)
            if i >= k-1:
                if balance == 1:
                    ans.append(-left[0])
                else:
                    ans.append((-left[0] + right[0]) / 2)
        return ans

    def adjustBalance(self, left, right, balance, count):
        self.remove_invalid(left, right, count)
        if balance >= 2:
            heapq.heappush(right, -heapq.heappop(left))
            balance -= 2
        if balance < 0:
            heapq.heappush(left, -heapq.heappop(right))
            balance += 2
        self.remove_invalid(left, right, count)
        return balance

    def remove_invalid(self, left, right, count):
        while left and count[-left[0]] > 0:
            count[-left[0]] -= 1
            heapq.heappop(left)
        while right and count[right[0]] > 0:
            count[right[0]] -= 1
            heapq.heappop(right)