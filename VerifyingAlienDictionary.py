class Solution:
    def isAlienSorted(self, words, order):
        dic = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            if not self.check(words[i], words[i+1], dic):
                return False
        return True
    def check(self, word1, word2, dic):
        if word1 == word2:
            return True
        index = 0
        while index < min(len(word1), len(word2)):
            if word1[index] != word2[index]:
                break
            index += 1
        if index == len(word1):
            return True
        elif index == len(word2):
            return False
        else:
            return dic[word1[index]] < dic[word2[index]]