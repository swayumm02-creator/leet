class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            for j in range(n):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            max_area = max(max_area, self.largestRectangleArea(heights))
            
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area