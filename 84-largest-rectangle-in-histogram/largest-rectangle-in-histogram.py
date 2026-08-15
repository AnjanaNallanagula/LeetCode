class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max1 = -1

        for i in range(n):
            while (stack and heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                j = stack[-1] if stack else -1
                max1 = max(max1, h * (i - j - 1))
            stack.append(i)
        
        while stack:
            h = heights[stack.pop()]
            j = stack[-1] if stack else -1
            max1 = max(max1, h * (n - j - 1))
        
        return max1