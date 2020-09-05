# Using dynamic programming

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for y in range(n)] for x in range(m)]
        matrix[0][0] = 1
        
        for col in range(1, n):
            matrix[0][col] = matrix[0][col - 1]
        
        for row in range(1, m):
            matrix[row][0] = matrix[row - 1][0]
        
        for row in range(1,m):
            for col in range(1,n):
                matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]
                
        return matrix[m-1][n-1]