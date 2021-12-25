import collections
class Solution:
    def wordSquares(self, words):
        ans = []
        prefix_dic = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                prefix_dic[word[:i + 1]].append(word)
        for word in words:
            self.backTrack(words, [word], prefix_dic, ans)
        return ans

    def backTrack(self, words, tmp, prefix_dic, ans):
        if len(tmp) == len(words[0]):
            ans.append(tmp)
            return
        prefix = ""
        index = len(tmp)
        for word in tmp:
            prefix += word[index]
        choices = prefix_dic[prefix]
        for choice in choices:
            self.backTrack(words, tmp + [choice], prefix_dic, ans)