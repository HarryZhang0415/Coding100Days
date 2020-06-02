'''
Approach 1 : Transpose and then reverse
The obvious idea would be to transpose the matrix first and then reverse each row. This simple approach already demonstrates the best possible time complexity O(N^2)
'''
class Solution:
    def rotate(self,matrix):
        '''
        :type matrix:List[List[int]]
        :rtype void Do not return anything, modify matrix in-place instead.
        '''

        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i,n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        for i in range(n):
            matrix[i].reverse()

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]]    
s = Solution()
s.rotate(matrix)