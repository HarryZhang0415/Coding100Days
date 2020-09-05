class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows, self.cols, self.diag, self.anti_diag = [0] * n, [0] * n, 0, 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.rows[row] += 1 if player == 2 else -1
        self.cols[col] += 1 if player == 2 else -1
        
        if row == col:
            self.diag += 1 if player == 2 else -1
        
        if row + col == self.n - 1:
            self.anti_diag += 1 if player == 2 else -1
        
        if self.n in self.rows or self.n in self.cols or self.n in [self.diag, self.anti_diag]:
            return 2
        
        if -self.n in self.rows or -self.n in self.cols or -self.n in [self.diag, self.anti_diag]:
            return 1
        
        return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)