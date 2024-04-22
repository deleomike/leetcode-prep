class Solution:
    def solution(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_area = None

        while l < r:
            left = heights[l]
            right = heights[r]
            area = (r - l) * min(left, right) 

            if max_area is None:
                max_area = area
            else:
                max_area = max(area, max_area)

            if left > right:
                r -= 1
            else:
                l += 1

        return max_area

    def maxArea(self, height: List[int]) -> int:
        return self.solution(height)