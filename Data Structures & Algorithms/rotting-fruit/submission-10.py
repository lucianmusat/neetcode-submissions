import copy

class Solution:
    # We do a loop through the whole matrix until all the fruits are rotten
    # If we find a fresh fruit, we do a check of the neighbors to check if there is any
    # rotten fruit, if yes then we make it rotten and set a flag that at least one fruit 
    # got rotten
    # At the end, if the flag is up we increment min_days, or else we reset the flag

    def valid_cell(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def hasRottenNeighbor(self, grid, row, col):
        if self.valid_cell(grid, row - 1, col) and grid[row - 1][col] == 2:
            return True
        if self.valid_cell(grid, row, col - 1) and grid[row][col - 1] == 2:
            return True
        if self.valid_cell(grid, row + 1, col) and grid[row + 1][col] == 2:
            return True
        if self.valid_cell(grid, row, col + 1) and grid[row][col + 1] == 2:
            return True    
        return False

    def has_fresh_fruit(self, grid):
        for row in grid:
            if 1 in row:
                return True
        return False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        min_days = 0
        fruit_rotted = False
        while True:
            grid_copy = copy.deepcopy(grid)
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1 and self.hasRottenNeighbor(grid_copy, row, col):
                        grid[row][col] = 2
                        fruit_rotted = True
            print(f"Loop finished. Current status: {grid}")
            if fruit_rotted:
                if min_days == -1:
                    min_days = 0
                min_days += 1
                fruit_rotted = False
            else:
                break
        if self.has_fresh_fruit(grid):
            min_days = -1
        return min_days
        