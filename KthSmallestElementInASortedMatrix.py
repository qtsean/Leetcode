import heapq


# TIME COMPLEXITY N + KLog(N)
class Solution:
    def kthSmallest(self, matrix, k):
        heap = []
        for i in range(min(k, len(matrix))):
            heap.append([matrix[i][0], i, 0])
        heapq.heapify(heap)
        while k > 0:
            cur, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, [matrix[i][j + 1], i, j + 1])
            k -= 1
        return cur


class Solution2:
    def kthSmallest(self, matrix, k):
        start = matrix[0][0]
        end = matrix[-1][-1]
        while start < end:
            mid = (start + end) // 2
            count, smaller, larger = self.countSmaller(matrix, mid)
            if count > k:
                end = smaller
            elif count < k:
                start = larger
            elif count == k:
                return smaller
        return start

    def countSmaller(self, matrix, number):
        smaller = matrix[0][0]
        larger = matrix[-1][-1]
        row = len(matrix) - 1
        col = 0
        count = 0
        while row >= 0 and col < len(matrix[0]):
            if number >= matrix[row][col]:
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

            else:
                larger = min(larger, matrix[row][col])
                row -= 1
        return count, smaller, larger
