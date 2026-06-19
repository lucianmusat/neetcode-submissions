class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or len(board) == 0:
            return
        rows, cols = len(board), len(board[0])
        visited = set()
        
        # mark all "O" cells as "T"
        def dfs(row, col):
            if row not in range(0, rows) or col not in range(0, cols):
                return
            if (row, col) in visited:
                return
            if board[row][col] == "O":
                visited.add((row, col))
                board[row][col] = "T"
                dfs(row - 1, col)
                dfs(row + 1, col)
                dfs(row, col - 1)
                dfs(row, col + 1)

        # Iterate edges, and do DFS on any "O" there, mark them
        # as a temporary letter "T"
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0 or row == (rows - 1) or col == (cols -1)) and board[row][col] == "O":
                    dfs(row, col)
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"
