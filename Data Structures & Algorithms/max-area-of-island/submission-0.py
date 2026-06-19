class Solution:

    def dfs(self, r: int, c: int, grid: list) -> int:
        validRow = 0 <= r < len(grid)
        validColumn = 0 <= c < len(grid[0])
        if not validRow or not validColumn:
            return 0
        
        if grid[r][c] == 0:
            return 0

        area = 1
        grid[r][c] = 0
        area += self.dfs(r - 1, c, grid)
        area += self.dfs(r + 1, c, grid)
        area += self.dfs(r, c - 1, grid)
        area += self.dfs(r, c + 1, grid)
        return area
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                maxArea = max(maxArea, self.dfs(row, col, grid))
        return maxArea
