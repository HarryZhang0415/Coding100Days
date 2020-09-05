class Solution:
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i] 


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]]    
s = Solution()
s.rotate(matrix)