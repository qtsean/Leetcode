class Solution:
    def wordPattern(self, pattern, s):
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        dic_s2pattern = {}
        dic_pattern2S = {}
        for index in range(len(pattern)):
            if s[index] not in dic_s2pattern and pattern[index] not in dic_pattern2S:
                dic_s2pattern[s[index]] = pattern[index]
                dic_pattern2S[pattern[index]] = s[index]
            elif s[index] in dic_s2pattern and pattern[index] in dic_pattern2S and dic_s2pattern[s[index]] == pattern[index] and dic_pattern2S[pattern[index]] == s[index]:
                continue
            else:
                return False
        return True

