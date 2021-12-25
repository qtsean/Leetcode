class Solution:
    def maximizeSweetness(self, sweetness, k):
        people = k + 1
        start = min(sweetness)
        end = sum(sweetness) // people
        while start <= end:
            mid = (start + end) // 2
            count = 0
            s = 0
            for sweet in sweetness:
                s += sweet
                if s >= mid:
                    s = 0
                    count += 1
            if count >= people:
                start = mid + 1
            else:
                end = mid - 1
        return end