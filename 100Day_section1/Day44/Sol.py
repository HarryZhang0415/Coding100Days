class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        self.ans = []
        
        def search(row, col, matrix, flag):
            if row < 0 or row >= len(matrix):
                return
            if col < 0 or col >= len(matrix[0]):
                return
            if matrix[row][col] == float('inf'):
                return
            
            self.ans.append(matrix[row][col])
            matrix[row][col] = float('inf')
            
            search(row + self.direction[flag][0], col + self.direction[flag][1], matrix, flag)
            search(row + self.direction[(flag + 1) % 4][0], col + self.direction[(flag + 1) % 4][1], matrix, (flag + 1) % 4)
            search(row + self.direction[(flag + 2) % 4][0], col + self.direction[(flag + 2) % 4][1], matrix, (flag + 2) % 4)
            search(row + self.direction[(flag + 3) % 4][0], col + self.direction[(flag + 3) % 4][1], matrix, (flag + 3) % 4)
        
        search(0, 0, matrix, 0)
        
        return self.ans
            