class Solution:

    grid = []
    # We can remove the need for this by modifying the grid directly
    visited = set()

    def dfs(self, r, c) -> bool:
        rowInBounds = 0 <= r < len(self.grid)
        columnInBounds = 0 <= c < len(self.grid[0])
        if not rowInBounds or not columnInBounds:
            return False

        if (self.grid[r][c] == "0"):
            return False

        pos = f"{r},{c}"  # using string to avoid object reference comparison
        if pos in self.visited:
            return False

        self.visited.add(pos)
        # We only need to explore to mark them as visited
        self.dfs(r, c - 1)
        self.dfs(r + 1, c)
        self.dfs(r, c + 1)
        self.dfs(r - 1, c)

        # Found a new island, we should return True
        return True


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        self.grid = grid
        island_count = 0
        self.visited = set()  # Reset for each call

        for row, _ in enumerate(grid):
            for column, _ in enumerate(grid[0]):  # Important!
                if self.dfs(row, column):
                    island_count += 1
        return island_count
        