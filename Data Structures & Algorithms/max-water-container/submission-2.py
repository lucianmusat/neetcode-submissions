class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        l,r = 0, len(heights) - 1
        while l < r:
            water_volume = (r - l) * min(heights[l], heights[r])
            max_volume = max(max_volume, water_volume)
            # Move pointers based on which line is smaller
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_volume
