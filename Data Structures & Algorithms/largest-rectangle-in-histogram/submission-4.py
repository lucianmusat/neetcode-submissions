class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest_rectangle = 0
        stack = []

        # Check if the rectangle hieghts are monotonic, if we find one that is smaller
        # than the previous, we pop it and calculate it's area.
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                last_rectangle_index, last_rectangle_height = stack.pop()
                biggest_rectangle = max(biggest_rectangle, last_rectangle_height * (i - last_rectangle_index))
                start = last_rectangle_index
            stack.append((start, height))
        
        # We are left with only monotonic.
        # Go through remaining items in the stack, calculating the area and comparing to the max
        for i, h in stack:
            biggest_rectangle = max(biggest_rectangle, h * (len(heights) - i))

        return biggest_rectangle