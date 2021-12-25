class NumArray:

    def __init__(self, nums):
        self.presum = [0]
        for n in nums:
            self.presum.append(n + self.presum[-1])

    def sumRange(self, left, right):
        return self.presum[right+1] - self.presum[left]
