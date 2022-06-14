from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = [len(heights)-1]
        for i in range(len(heights)):
            index = len(heights) - i - 1
            if heights[index] > heights[ans[-1]]:
                ans.append(index)
        return ans[::-1]

if __name__ == '__main__':
    heights = [4,2,3,1]
    s = Solution()
    print(s.findBuildings(heights))
