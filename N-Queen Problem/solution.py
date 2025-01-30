class Solution:
    def nQueen(self, n):
        def is_safe(row, col, board):
            for i in range(col):
                if board[i] == row or abs(board[i] - row) == abs(i - col):
                    return False
            return True

        def solve(col, board, result):
            if col == n:
                result.append([x + 1 for x in board])
                return
            for row in range(n):
                if is_safe(row, col, board):
                    board[col] = row
                    solve(col + 1, board, result)
                    board[col] = -1

        result = []
        board = [-1] * n
        solve(0, board, result)
        return result
    
"""
Summary
1. is_safe Function: This function checks if placing a queen at a specific row and column is safe by ensuring no other queen is in the same row or diagonal.
2. solve Function: This is the recursive backtracking function. It tries to place a queen in each column and checks if the placement is safe. If it is, it proceeds to the next column. If not, it backtracks and tries a different row.
3. Result Collection: When a valid configuration is found (all queens are placed safely), the configuration is added to the result list.
4. Initialization: The board array is initialized with -1 to represent no queen placed. The solve function is called starting from the first column.

The time complexity is O(n!) due to the backtracking nature of the problem, and the space complexity is O(n) for the recursion stack and the board representation.
"""