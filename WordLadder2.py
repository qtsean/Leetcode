import collections


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        used = set()
        neighbors = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                tmp = word[: i] + "_" + word[i+1:]
                neighbors[tmp].append(word)
        queue = [[beginWord]]
        used.add(beginWord)
        ans = []
        found = False
        while queue:
            tmp = []
            new_nodes = set()
            for path in queue:
                word = path[-1]
                if word == endWord:
                    found = True
                    ans.append(path)
                for i in range(len(word)):
                    cur = word[:i] + "_" + word[i+1:]
                    for neighbor in neighbors[cur]:
                        if neighbor not in used:
                            tmp.append(path+[neighbor])
                            new_nodes.add(neighbor)
            used = used.union(new_nodes)
            queue = tmp
            if found:
                break
        return ans