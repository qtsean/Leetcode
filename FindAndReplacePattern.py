class Solution:
    def findAndReplacePattern(self, words, pattern):
        ans = []
        for word in words:
            if self.checkMatch(word, pattern):
                ans.append(word)
        return ans

    def checkMatch(self, word, pattern):
        w2p = {}
        p2w = {}
        for i in range(len(word)):
            w = word[i]
            p = pattern[i]
            if w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p and p in p2w:
                return False
            elif w in w2p and p not in p2w:
                return False
            else:
                if w2p[w] != p or p2w[p] != w:
                    return False
        return True