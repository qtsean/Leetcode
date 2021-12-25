class Solution:
    def partitionLabels(self, s):
        right_most = {}
        for i, c in enumerate(s):
            right_most[c] = i
        indexes = [0]
        far = 0
        for i, c in enumerate(s):
            if i > far:
                indexes.append(i)
            far = max(far, right_most[c])
        indexes.append(len(s))
        ans = []
        for i in range(1, len(indexes)):
            ans.append(indexes[i] - indexes[i-1])
        return ans