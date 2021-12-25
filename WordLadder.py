import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        used = set()
        used.add(beginWord)
        queue = [beginWord]
        step = 1
        neighbors = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + "_" + word[i+1:]
                neighbors[tmp].append(word)

        while queue:
            tmp = []
            for word in queue:
                if word == endWord:
                    return step
                for i in range(len(word)):
                    cur = word[:i] + "_" + word[i+1:]
                    for neighbor in neighbors[cur]:
                        if neighbor not in used:
                            tmp.append(neighbor)
                            used.add(neighbor)
            step += 1
            queue = tmp
        return 0
                            