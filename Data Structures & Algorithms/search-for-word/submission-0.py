class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Basically do a dfs on all the letters of the board
        # Mark letters as explored, but reset them back at the end
        def backtrack(row, col, i) -> bool:
            # We got a valid solution. By the time we get here, all the chars have been validated.
            if i == len(word):
                return True
            # Check out of bounds
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i]:
                return False
            # Mark current cell to not chose again
            temp, board[row][col] = board[row][col], '*'
            # Explore all 4 directions
            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if backtrack(row + r, col + c, i + 1):
                    return True
            # Reset current cell
            board[row][col] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False