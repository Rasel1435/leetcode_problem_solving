
"""Intuition
The problem is asking to validate a partially filled Sudoku board. The rules of Sudoku state that each row,
each column, and each 3x3 grid must contain the digits 1-9 without repetition. So,
the intuition here is to check these three conditions for the given board.

Approach
1. Check Rows: For each row in the board, check if there are any duplicate numbers (ignoring the empty cells denoted by ".").
   If any duplicates are found, return False.

2. Check Columns: Similarly, for each column, check if there are any duplicate numbers.
   If any duplicates are found, return False.

3. Check 3x3 Grids: The 9x9 Sudoku board can be divided into nine 3x3 grids.
   For each of these grids, check if there are any duplicate numbers.
   If any duplicates are found, return False.
   
If no duplicates are found in any of the rows, columns, or 3x3 grids, then the given board is a valid Sudoku board, so return True.
"""


from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
    
if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))
    print(Solution().isValidSudoku(board))
    print(Solution().isValidSudoku(board))
    print(Solution().isValidSudoku(board))
    print(Solution().isValidSudoku(board))