class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 1:
            return 
        self.row = len(board)
        self.col = len(board[0])
        if self.row <= 2 or self.col <= 2:
            return
        
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == 'O' and \
                (i==0 or i==self.row-1 or j==0 or j==self.col-1):
                    self.dfs(i, j, board)
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '#': board[i][j] = 'O'
        
    def dfs(self, i, j, board):
        if i in range(self.row) and j  in range(self.col) and board[i][j] == 'O':
            board[i][j] = "#"
            self.dfs(i, j+1, board)
            self.dfs(i+1, j, board)
            self.dfs(i-1, j, board)
            self.dfs(i, j-1, board)
