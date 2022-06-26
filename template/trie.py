class Node:
    def __init__(self):
        # is_word表示这个结点是否为一个单词的结尾
        # next[]表示这个结点的下一个26个字母结点
        self.is_word = False
        self.next = [None] * 26


class Trie:

    def __init__(self):
        self.root = Node()

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        now = self.root
        length = len(word)
        for i in range(length):
            # 依次查找每个字符
            # 如果所有下一个结点中没有当前字符，则增加新结点到下一个next[pos]
            pos = ord(word[i]) - ord('a')
            if now.next[pos] is None:
                now.next[pos] = Node()
            now = now.next[pos]
        now.is_word = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        # 查找单词
        now = self.root
        n = len(word)
        for i in range(n):
            ch = ord(word[i]) - ord('a')
            # 如果有下一个对应字符的结点，那么继续查找下一个结点
            # 如果没有下一个对应字符的结点，那么说明查找单词失败
            if now.next[ch] != None:
                now = now.next[ch]
            else:
                return False
        # 如果每个字符都有且是完整单词，才说明查找单词成功
        return now.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        # 查找前缀
        now = self.root
        n = len(prefix)
        for i in range(n):
            ch = ord(prefix[i]) - ord('a')
            # 如果有下一个对应字符的结点，那么继续查找下一个结点
            # 如果没有下一个对应字符的结点，那么说明查找前缀失败
            if now.next[ch] != None:
                now = now.next[ch]
            else:
                return False
        return True