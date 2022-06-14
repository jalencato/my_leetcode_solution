class Solution:
    def __init__(self):
        self.long_word = ''

    def trie_split(self, words):
        trie = {"#": "#"}

        def dfs(trie, word):
            if trie == '#':
                return
            if '#' in trie:
                if len(self.long_word) < len(word) or \
                        (len(self.long_word) == len(word) and self.long_word > word):
                    self.long_word = word
                for c in trie:
                    dfs(trie[c], word + c)

        for w in words:
            t = trie
            for char in w:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t['#'] = '#'
        print(trie)
        dfs(trie, '')
        return self.long_word


if __name__ == '__main__':
    # words_1 = ['w', 'wo', 'wor', 'worl', 'world']
    words_2 = ['a', 'banana', 'app', 'appl', 'ap', 'apply', 'apple']
    s = Solution()
    # print(s.trie_split(words_1))
    print(s.trie_split(words_2))
