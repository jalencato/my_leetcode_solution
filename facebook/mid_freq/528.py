import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.weight = w
        self.length = len(w)
        self.box = []

        for i in w:
            self.box.append(i*1.0/sum(self.weight))

    def pickIndex(self) -> int:
        r = random.uniform(0, 1)
        #
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()