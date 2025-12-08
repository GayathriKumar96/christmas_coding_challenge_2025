"""
Question from  LeetCode:
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""

# Solution in Python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            row = [x for x in board[i][:] if x!='.']
            if len(row) != len(set(row)):
                print("row fail")
                return False
        for j in range(n):
            col = [board[i][j] for i in range(n) if board[i][j]!='.']
            if len(col) != len(set(col)):
                print("col fail")
                return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if board[r][c] != '.':
                            box.append(board[r][c])
                if len(box) != len(set(box)):
                    print("box fail")
                    return False       
        return True
        
