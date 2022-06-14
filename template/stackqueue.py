class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        stack = [-1]
        max_area = 0

        for i in range(n):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                h = stack.pop()
                max_area = max(max_area, heights[h] * (i - stack[-1] - 1))
            stack.append(i)

        while len(stack) > 1:
            h = stack.pop()
            max_area = max(max_area, heights[h] * (n - stack[-1] - 1))

        return max_area