"""
Approach 2 : Rotate four rectangles
Approach 1 makes two passes through the matrix, though it's possible to make a rotation in one pass.

To figure out how let's check how each element in the angle moves during the rotation.
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype void Do not return anything, modify matrix in-place instead
        """

        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                for k in range(4):
                    matrix[row][col] = tmp[(k-1)%4]
                    row, col = col, n - 1 - row

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]]    
s = Solution()
s.rotate(matrix)