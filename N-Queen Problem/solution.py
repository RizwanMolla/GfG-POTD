class Solution:
    def nQueen(self, n):
        def is_safe(row, col, board):
            for i in range(col):
                if board[i] == row or abs(board[i] - row) == abs(i - col):
                    return False
            return True

        def solve(col, board, result):
            if col == n:
                result.append([x + 1 for x in board])  # Convert to 1-based indexing
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