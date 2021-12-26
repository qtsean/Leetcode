class Solution:
    def canReach(self, arr, start):
        target = set([index for index, num in enumerate(arr) if num == 0])
        visited = set()
        visited.add(start)
        queue = [start]
        while queue:
            tmp = []
            for q in queue:
                if q in target:
                    return True
                left = q - arr[q]
                right = q + arr[q]
                if left >= 0 and left not in visited:
                    tmp.append(left)
                    visited.add(left)
                if right < len(arr) and right not in visited:
                    tmp.append(right)
                    visited.add(right)
            queue = tmp

        return False
