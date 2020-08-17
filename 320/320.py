from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []

        def helper(curr_pos, s, cnt):
            if curr_pos == len(word):
                if cnt > 0:
                    res.append(s + str(cnt))
                else:
                    res.append(s)
                return
            # number caller
            helper(curr_pos + 1, s, cnt + 1)
            # string caller
            if cnt > 0:
                helper(curr_pos + 1, s + str(cnt) + word[curr_pos], 0)
            else:
                helper(curr_pos + 1, s + word[curr_pos], 0)
        helper(0, "", 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateAbbreviations('word'))
