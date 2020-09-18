from collections import defaultdict


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        places = defaultdict(list)
        for i in reversed(range(len(s))):
            key = int(s[i])
            places[key].append(i)

        for e in t:
            key = int(e)
            if not places[key]:
                return False
            i = places[key][-1]
            for j in range(key):
                if places[j] and places[j][-1] < i:
                    return False
            places[key].pop()

        return True


if __name__ == '__main__':
    s = Solution()
    str1 = "84532"
    str2 = "34852"
