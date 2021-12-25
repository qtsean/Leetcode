import collections


class Solution:
    def possibleBipartition(self, n, dislikes):
        left = set()
        right = set()
        neighbors = collections.defaultdict(list)
        for p1, p2 in dislikes:
            neighbors[p1].append(p2)
            neighbors[p2].append(p1)
        def dfs(cur, isLeft):
            ans = True
            if cur in left:
                if isLeft:
                    return True
                else:
                    return False
            elif cur in right:
                if isLeft:
                    return False
                else:
                    return True
            else:
                if isLeft:
                    left.add(cur)
                else:
                    right.add(cur)
                for neighbor in neighbors[cur]:
                    ans = ans and dfs(neighbor, not isLeft)
            return ans

        for person in neighbors.keys():
            if person not in left and person not in right:
                if not dfs(person, True):
                    return False
        return True
