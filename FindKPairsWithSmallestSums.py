import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        total_pairs = len(nums1) * len(nums2)
        k = min(k, total_pairs)
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        heap = []
        used = set()
        s = nums1[0] + nums2[0]
        cols = [0, 0]
        used.add(tuple(cols))
        heap.append([s, tuple(cols)])
        ans = []
        while k > 0:
            s, cols = heapq.heappop(heap)
            cols = list(cols)
            ans.append([nums1[cols[0]], nums2[cols[1]]])
            new_cols1 = tuple([cols[0]+1, cols[1]])
            new_cols2 = tuple([cols[0], cols[1] + 1])
            if new_cols1 not in used:
                heapq.heappush(heap, [nums1[new_cols1[0]] + nums2[new_cols1[1]], new_cols1])
                used.add(new_cols1)
            if new_cols2 not in used:
                heapq.heappush(heap, [nums1[new_cols2[0]] + nums2[new_cols2[1]], new_cols2])
                used.add(new_cols2)
            k -= 1
        return ans


