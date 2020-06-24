# Dynamic programming --> accepted

import math

class Solution:
    def numSquares(self, n: int) -> int:
        squares_nums = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        
        self.ans = {i: float('inf') for i in range(1, n+1)}
        self.ans[0] = 0 
        
        for i in range(1,n+1):
            for squares in squares_nums:
                if i < squares:
                    break
                self.ans[i] = min(self.ans[i], self.ans[i-squares] + 1)
            
        return self.ans[n]
                
