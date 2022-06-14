from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        priority = {}
        for char in order:
            priority[char] = len(priority)

        for word1, word2 in zip(words, words[1:]):
            for char1, char2 in zip(word1, word2):
                if char1 == char2:
                    continue
                else:
                    if priority[char1] > priority[char2]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True


if __name__ == '__main__':
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"

    s = Solution()
    print(s.isAlienSorted(words, order))