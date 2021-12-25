import collections


class Node:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(Node)

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return True
