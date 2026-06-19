class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(row, col, visited, previousHeight):
            if (
                (row, col) in visited or 
                row not in range(0, ROWS) or 
                col not in range(0, COLS) or 
                heights[row][col] < previousHeight
            ):
                return
            visited.add((row, col))
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])

        # Top and bottom borders
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])  # Top row for Pacific
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])  # Bottom row for Atlantic

        # Left and right borders for Pacific and Atlantic respectively
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])  # Left column for Pacific
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])  # Right column for Atlantic
        
        return list(pacific.intersection(atlantic))