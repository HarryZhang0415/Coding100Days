# Sol 1: recursion --> time exceeding, not accepted

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.ans = float('inf')
        def search(grid, tmp_sum, row, col):
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                tmp_sum += grid[row][col]
                self.ans = min(self.ans, tmp_sum)
                return
            
            if row >= len(grid) or col >= len(grid[0]):
                return
            else:
                search(grid, tmp_sum + grid[row][col], row + 1, col)
                search(grid, tmp_sum + grid[row][col], row, col + 1)
        
        search(grid,0,0,0)
        return self.ans

# Sol 2: recursion solution in the answer blog --> time exceeding, not accepted

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def search(grid, row, col):
            if row >= len(grid) or col >= len(grid[0]):
                return float('inf')
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
            
            return grid[row][col] + min(search(grid, row + 1, col), search(grid, row, col + 1))
        
        return search(grid, 0, 0)

# Try same solution under Java --> not accepted due to time exceeding

# Sol 3: Dynamic programming in Java
