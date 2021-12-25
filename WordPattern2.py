class Solution:
    def wordPatternMatch(self, pattern, s):
        return self.dfs(pattern, 0, s, 0, {}, {})

    def dfs(self, p, p_index, s, s_index, dic_s2p, dic_p2s):
        if p_index == len(p) and s_index == len(s):
            return True
        elif p_index == len(p) or s_index == len(s):
            return False
        if p[p_index] in dic_p2s:
            word = dic_p2s[p[p_index]]
            if s_index + len(word) - 1 < len(s):
                if word == s[s_index: s_index + len(word)]:
                    return self.dfs(p, p_index+1, s, s_index+len(word), dic_s2p, dic_p2s)
                else:
                    return False
            else:
                return False
        else:
            length = 1
            res = False
            while s_index + length - 1 < len(s):
                word = s[s_index: s_index+length]
                if word not in dic_s2p:
                    dic_s2p[word] = p[p_index]
                    dic_p2s[p[p_index]] = word
                    res = res or self.dfs(p, p_index+1, s, s_index+len(word), dic_s2p, dic_p2s)
                    if res:
                        break
                    dic_s2p.pop(word)
                    dic_p2s.pop(p[p_index])
                length += 1
            return res
