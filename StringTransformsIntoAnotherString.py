class Solution:
    def canConvert(self, str1: str, str2: str):
        if str1 == str2:
            return True
        dic = {}
        used = set()
        for i in range(len(str1)):
            c1 = str1[i]
            c2 = str2[i]
            if c1 not in dic:
                used.add(c2)
                dic[c1] = c2
            elif dic[c1] != c2:
                return False
        count = 0
        visited = set()
        for key in dic.keys():
            if key in visited:
                continue
            else:
                while key in dic.keys() and key not in visited:
                    visited.add(key)
                    key = dic[key]
                if key not in dic.keys():
                    continue
                else:
                    count += 1
        return count + len(dic.keys())

s = Solution()
print(s.canConvert("abcdef", "cabefd"))