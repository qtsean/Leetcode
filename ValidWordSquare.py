class Solution:
    def validWordSquare(self, words):
        for i in range(len(words)):
            word = words[i]
            tmp = ""
            count = 0
            for w in words:
                if count == len(word):
                    break
                if i >= len(w):
                    return False
                tmp += w[i]
                count += 1
            if tmp != word:
                return False
        return True

s = Solution()
s.validWordSquare(["abcd","bnrt","crm","dt"])