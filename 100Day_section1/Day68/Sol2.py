class Solution:
    def __init__(self):
        self.dir = []
        self.n_rows = 0
        
    def direction(self, row, col):
        self.dir.append((row, col))
        if row == 0:
            return (row+1, col)
        elif row == self.n_rows - 1:
            return (row - 1, col + 1)
        else:
            if (row-1,col) not in self.dir:
                return (row - 1, col + 1)
            else:
                return (row + 1, col)
        
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        matrix = [['' for i in range(len(s))] for i in range(numRows)]
        self.n_rows = numRows
        
        row, col = 0,0
        
        for idx in range(len(s)):
            matrix[row][col] = s[idx]
            row, col = self.direction(row,col)
        
        ans = ''
        
        for line in matrix:
            ans += "".join(line)
        
        return ans

# Using Hash map to solve the question
'''class Solution:
    def __init__(self):
        self.dir = []
        self.n_rows = 0
        
    def direction(self, row, col):
        self.dir.append((row, col))
        if row == 0:
            return (row+1, col)
        elif row == self.n_rows - 1:
            return (row - 1, col + 1)
        else:
            if (row-1,col) not in self.dir:
                return (row - 1, col + 1)
            else:
                return (row + 1, col)
        
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        matrix = collections.defaultdict(str)
        self.n_rows = numRows
        
        row, col = 0,0
        
        for idx in range(len(s)):
            matrix[row] += s[idx]
            row, col = self.direction(row,col)
        
        ans = ''
        
        for _ in sorted(matrix.keys()):
            ans += matrix[_]
        
        return ans'''