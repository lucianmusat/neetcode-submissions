class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        # Secret sauce, use a few sets to "remember" if other queens
        # have been placed in attacking positions
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n) ]

        def valid_location(row: int, col: int) -> bool:
            if col in cols or (row - col) in pos_diag or (row + col) in neg_diag:
                return False
            return True

        def backtrack(row: int) -> None:
            # base case - we reached n + 1 row, means we succesfully placed
            # all the queens
            if row == n:
                solutions.append(["".join(cell) for cell in board])
                return

            # explore posibilities
            # we go column by column, and increment row
            for col in range(n):
                if valid_location(row, col):
                    # chose
                    cols.add(col)
                    pos_diag.add(row - col) # all positive diagonals have the same r - c value
                    neg_diag.add(row + col) # all negative diagonals have the same r + c value
                    board[row][col] = 'Q'
                    # explore
                    backtrack(row + 1)
                    # backtrack
                    cols.remove(col)
                    pos_diag.remove(row - col)
                    neg_diag.remove(row + col)
                    board[row][col] = '.'

        solutions = []
        backtrack(0)
        return solutions