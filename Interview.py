import collections


class Node:
    def __int__(self):
        self.cnt = 0
        self.children = collections.defaultdict()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node.cnt += 1
            node = node.children[w]
        node.cnt += 1

    def prefixHelper(self, word):
        node = self.root
        path = []
        for w in word:
            if w not in node.children:
                return ""

            node = node.children[w]
            path.append(w)
            if node.cnt == 1:
                return ''.join(path)

            return "hahaha"


class Solution:
    def ShortPerfix(self, stringArray):
        trie = Trie()
        for string in stringArray:
            trie.insert(string)

        return [trie.prefixHelper(s) for s in stringArray]