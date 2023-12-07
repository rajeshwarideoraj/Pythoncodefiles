class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_valid(board, row, col):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check if there is a queen in the left upper diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check if there is a queen in the right upper diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def solveNQueensHelper(board, row, result):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    solveNQueensHelper(board, row + 1, result)
                    board[row][col] = '.'  # backtrack
        
        result = []
        # Initialize the chessboard with empty spaces
        board = [['.' for _ in range(n)] for _ in range(n)]
        solveNQueensHelper(board, 0, result)
        return result
        