class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = [[0 for i in range(len(board[0])+2)] for j in range(len(board)+2)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                matrix[row + 1][col + 1] = board[row][col]
        
        def judge(matrix, row, col):
            neighbor = [matrix[row-1][col-1],matrix[row-1][col],matrix[row-1][col+1],
                        matrix[row][col-1],matrix[row][col+1],
                        matrix[row+1][col-1],matrix[row+1][col],matrix[row+1][col+1]]
            
            if sum(neighbor) < 2:
                return 0
            elif matrix[row][col] == 1 and (sum(neighbor) == 2 or sum(neighbor) == 3):
                return 1
            elif sum(neighbor) > 3:
                return 0
            elif matrix[row][col] == 0 and sum(neighbor) == 3:
                return 1
            else:
                return 0
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = judge(matrix, row + 1,col + 1)
        
        
                
            