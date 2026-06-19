from collections import deque

class Solution:
    INF = 2147483647

    def valid_cell(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != -1
    
    def distanceToNearestTreasure(self, grid, row, column):  # BFS algo to find the closest 0
        queue = deque([(row, column)])
        visited = set((row, column))
        min_distance = 0
    
        while queue:
            for _ in range(len(queue)):  # process all cells on a certain level before incrementing min_distance
                row, col = queue.popleft()
                if self.valid_cell(row, col, grid) and (row, col) not in visited:
                    visited.add((row, col))
                    if grid[row][col] == 0:
                        return min_distance
                    queue.append((row - 1, col))
                    queue.append((row + 1, col))
                    queue.append((row, col - 1))
                    queue.append((row, col + 1))
            min_distance += 1

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == self.INF:
                    grid[row][column] = self.distanceToNearestTreasure(grid, row, column)
        