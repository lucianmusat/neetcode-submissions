class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_block(block: list[str]) -> bool:
            no_empty_spots = [elem for elem in block if elem != '.']
            return len(no_empty_spots) + 1 == len(set(block))

        # check all rows
        for row in board:
            if not valid_block(row):
                return False
        
        # check all columns
        for col in zip(*board):
            if not valid_block(col):
                return False
        
        # check sub-blocks
        for i in range(0, 9, 3): # from 0..9 in steps of 3
            for j in range(0, 9, 3):
                sub_block = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not valid_block(sub_block):
                    return False
        
        return True