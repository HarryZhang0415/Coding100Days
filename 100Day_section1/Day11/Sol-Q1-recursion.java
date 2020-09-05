// Still error, time exceeding ---> not accepted
class Solution {
    public int minPathSum(int[][] grid) {
        return calculate(grid,0,0);
    }
    
    public int calculate(int[][] grid, int row, int col){
        if(row >= grid.length || col >= grid[0].length) return Integer.MAX_VALUE;
        if (row == grid.length - 1 && col == grid[0].length - 1) return grid[row][col];
        return grid[row][col] + Math.min(calculate(grid, row+1,col), calculate(grid, row, col+1));
    }
}

// Solution 2 dynamic programming
// class Solution {
//     public int minPathSum(int[][] grid) {
//         int[][] dp = new int[grid.length][grid[0].length];
//         for(int i = grid.length - 1; i >= 0; i--){
//             for(int j = grid[0].length - 1; j >= 0; j--){
//                 if(i == grid.length - 1 && j != grid[0].length - 1)
//                     dp[i][j] = grid[i][j] + dp[i][j + 1];
//                 else if(j == grid[0].length - 1 && i != grid.length - 1)
//                     dp[i][j] = grid[i][j] + dp[i+1][j];
//                 else if(j != grid[0].length - 1 && i != grid.length - 1)
//                     dp[i][j] = grid[i][j] + Math.min(dp[i+1][j], dp[i][j+1]);
//                 else
//                     dp[i][j] = grid[i][j];
//             }
//         }
//         return dp[0][0];
//     }
// }

// Solution 3 dynamic programming with only columns

// public class Solution {
//     public int minPathSum(int[][] grid) {
//         int[] dp = new int[grid[0].length];
//         for (int i = grid.length - 1; i >= 0; i--) {
//             for (int j = grid[0].length - 1; j >= 0; j--) {
//                 if(i == grid.length - 1 && j != grid[0].length - 1)
//                     dp[j] = grid[i][j] +  dp[j + 1];
//                 else if(j == grid[0].length - 1 && i != grid.length - 1)
//                     dp[j] = grid[i][j] + dp[j];
//                 else if(j != grid[0].length - 1 && i != grid.length - 1)
//                     dp[j] = grid[i][j] + Math.min(dp[j], dp[j + 1]);
//                 else
//                     dp[j] = grid[i][j];
//             }
//         }
//         return dp[0];
//     }
// }