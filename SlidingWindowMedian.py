import collections
import heapq


class Solution:
    def medianSlidingWindow(self, nums, k):
        left = []
        right = []
        ans = []
        count = collections.defaultdict(int)
        balance = 0
        for i in range(len(nums)):
            if i >= k:
                out_num = nums[i-k]
                count[out_num] += 1
                if out_num <= -left[0]:
                    balance -= 1
                else:
                    balance += 1
            if not left or nums[i] <= -left[0]:
                heapq.heappush(left, -nums[i])
                balance += 1
            else:
                heapq.heappush(right, nums[i])
                balance -= 1
            balance = self.balanceHeaps(left, right, balance)
            while left and count[-left[0]] > 0:
                count[-left[0]] -= 1
                heapq.heappop(left)
            while right and count[right[0]] > 0:
                count[right[0]] -= 1
                heapq.heappop(right)
            if i >= k - 1:
                if balance == 0:
                    ans.append((-left[0] + right[0]) / 2)
                else:
                    ans.append(-left[0])
        return ans

    def balanceHeaps(self, left, right, balance):
        while balance >= 2:
            number = heapq.heappop(left)
            heapq.heappush(right, -number)
            balance -= 2
        while balance <= -1:
            number = heapq.heappop(right)
            heapq.heappush(left, -number)
            balance += 2
        return balance