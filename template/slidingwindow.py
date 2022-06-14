import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = collections.defaultdict(int)

        for c in s1:
            target[c] += 1

        r, num_char = 0, len(target)

        while r < len(s2):
            if s2[r] in target:
                l, count = r, 0
                window = collections.defaultdict(int)
                while r < len(s2):
                    c = s2[r]
                    if c not in target:
                        break
                    window[c] += 1
                    if window[c] == target[c]:
                        count += 1
                        if count == num_char:
                            return True
                    while window[c] > target[c]:
                        window[s2[l]] -= 1
                        if window[s2[l]] == target[s2[l]] - 1:
                            count -= 1
                        l += 1
                    r += 1
            else:
                r += 1

        return False