# Approach (Dynamic Programming) [Accepted]

'''Algorithm

https://leetcode.com/problems/maximal-square/solution/

We will explain this approach with the help of an example.

0 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 1 1 1 1
0 0 1 1 1
We initialize another matrix (dp) with the same dimensions as the original one initialized with all 0’s.

dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.

Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as

\text{dp}(i, j) = \min \big( \text{dp}(i-1, j), \text{dp}(i-1, j-1), \text{dp}(i, j-1) \big) + 1.dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.

We also remember the size of the largest square found so far. In this way, we traverse the original matrix once and find out the required maximum size. This gives the side length of the square (say maxsqlenmaxsqlen). The required result is the area maxsqlen^2maxsqlen 
2
 .
'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        
        ans = 0
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if matrix[row - 1][col - 1] == '1':
                    dp[row][col] = min(dp[row - 1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    ans = max(ans, dp[row][col])
        
        return ans * ans
