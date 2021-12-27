import collections


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.count_self = 0
        self.count_start = 0
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
            node.count_start += 1
        node.count_self += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for w in word:
            node = node.children[w]
        return node.count_self

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for w in prefix:
            node = node.children[w]
        return node.count_start

    def erase(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
            node.count_start -= 1
        node.count_self -= 1

    def search(self, prefix):
        node = self.root
        for w in prefix:
            node = node.children[w]
        ans = []
        self.dfs(node, ans, prefix, [])
        return ans

    def dfs(self, node, ans, prefix, tmp):
        if node.count_self > 0:
            ans.append(prefix + "".join(tmp))
        if node.count_start > 0:
            for c in node.children.keys():
                self.dfs(node.children[c], ans, prefix, tmp+[c])

trie = Trie()
trie.insert("a")
trie.insert("ab")
trie.insert("abc")
trie.insert("abcd")
print(trie.countWordsStartingWith("ab"))
print(trie.search("ab"))
trie.erase("abc")
print(trie.countWordsStartingWith("ab"))
print(trie.search("ab"))
