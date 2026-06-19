class Solution {

    private boolean dfs(char[][] grid, int row, int col) {
        if (row < 0 || col < 0 || row > grid.length - 1 
            || col > grid[0].length - 1) {
                return false;
        }
        if (grid[row][col] == '0') {
            return false;
        }
        grid[row][col] = '0';
        dfs(grid, row + 1, col);
        dfs(grid, row - 1, col);
        dfs(grid, row, col + 1);
        dfs(grid, row, col - 1);
        return true;
    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int nrOfIslands = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++)
                if (dfs(grid, i, j)) {
                    nrOfIslands++;
                }
        }
        return nrOfIslands;
    }
}
