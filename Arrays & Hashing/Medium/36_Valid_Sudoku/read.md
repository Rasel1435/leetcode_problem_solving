
# Intuition
The problem is asking to validate a partially filled Sudoku board. The rules of Sudoku state that each row,
each column, and each 3x3 grid must contain the digits 1-9 without repetition. So,
the intuition here is to check these three conditions for the given board.

# Approach
- Check Rows: For each row in the board, check if there are any duplicate numbers (ignoring the empty cells
denoted by "."). If any duplicates are found, return False.

- Check Columns: Similarly, for each column, check if there are any duplicate numbers.
If any duplicates are found, return False.

- Check 3x3 Grids: The 9x9 Sudoku board can be divided into nine 3x3 grids.
For each of these grids, check if there are any duplicate numbers. If any duplicates are found, return False.
   
If no duplicates are found in any of the rows, columns, or 3x3 grids, then the given board is a valid Sudoku board, so return True.
"""

# Code:
```
from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """This line defines a method isValidSudoku inside the Solution class. The method takes a 2D list (List[List[str]])
           representing the Sudoku board as input and returns a boolean (bool). It checks whether the given Sudoku board is valid."""
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r // 3, c // 3)
        """Here, three defaultdicts are initialized: cols, rows, and squares. These will be used to keep track of the numbers
           present in each column, each row, and each 3x3 subgrid of the Sudoku board, respectively."""

        for r in range(9):
            for c in range(9):
        # These lines initiate nested loops to iterate over each cell in the 9x9 Sudoku board.
                if board[r][c] == ".":
                    continue
                """This conditional statement checks if the current cell contains a dot (.), which represents an empty cell in the Sudoku board.
                   If it does, the loop continues to the next iteration, skipping the rest of the code for the current cell."""
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]
                    ):
                    return False
                """ This block checks if the current number in the Sudoku board is already present in the corresponding row, column,
                or 3x3 subgrid. If it is, the Sudoku board is invalid, and the method returns False."""
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                """ If the current number is not present in the corresponding row, column, or subgrid,
                it is added to the sets in cols, rows, and squares, respectively."""

        return True
        """If the Sudoku board is valid, the method returns True."""
    
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
    
```