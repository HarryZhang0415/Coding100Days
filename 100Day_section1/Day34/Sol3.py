# Approach 3: Greedy Enumeration
# Solution link: https://leetcode.com/problems/perfect-squares/solution/
import math
class Solution:
    def numSquares(self, n: int) -> int:
        self.square_num = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        
        def greedy(number, count):
            if count == 1:
                return number in self.square_num
            
            for square in self.square_num:
                if greedy(number - square, count - 1):
                    return True
            
            return False
        
        for count in range(1, n+1):
            if greedy(n, count):
                return count
            