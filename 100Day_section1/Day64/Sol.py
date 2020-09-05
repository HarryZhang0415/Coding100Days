class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = [[0 for i in range(len(board[0]) + 2)] for j in range(len(board) + 2)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                matrix[row + 1][col + 1] = board[row][col]
        
        for row in range(1, len(matrix) - 1):
            for col in range(1, len(matrix[0]) - 1):
                neighbor = [matrix[row - 1][col - 1], matrix[row][col - 1], matrix[row+1][col - 1], matrix[row - 1][col], matrix[row + 1][col], matrix[row-1][col+1], matrix[row][col+1], matrix[row+1][col+1]]                
                if sum(neighbor) < 2 and matrix[row][col] == 1:
                    board[row - 1][col - 1] = 0
                elif (sum(neighbor) == 2 or sum(neighbor) == 3) and matrix[row][col] == 1:
                    board[row - 1][col - 1] = 1
                elif sum(neighbor) > 3 and matrix[row][col] == 1:
                    board[row - 1][col - 1] = 0
                elif sum(neighbor) == 3 and matrix[row][col] == 0:
                    board[row - 1][col - 1] = 1
                else:
                    continue
        
        
        
'''Folow up questions:

Q1: Using other numbers to represent the status like using 2 for next live

Q2:

The problem statement also mentions another follow-up statement which is a bit open ended. We will look at two possible solutions to address it. Essentially, the second follow-up asks us to address the scalability aspect of the problem. What would happen if the board is infinitely large? Can we still use the same solution that we saw earlier or is there something else we will have to do different? If the board becomes infinitely large, there are multiple problems our current solution would run into:

It would be computationally impossible to iterate a matrix that large.
It would not be possible to store that big a matrix entirely in memory. We have huge memory capacities these days i.e. of the order of hundreds of GBs. However, it still wouldn't be enough to store such a large matrix in memory.
We would be wasting a lot of space if such a huge board only has a few live cells and the rest of them are all dead. In such a case, we have an extremely sparse matrix and it wouldn't make sense to save the board as a "matrix".
Such open ended problems are better suited to design discussions during programming interviews and it's a good habit to take into consideration the scalability aspect of the problem since your interviewer might be interested in talking about such problems. The discussion section already does a great job at addressing this specific portion of the problem. We will briefly go over two different solutions that have been provided in the discussion sections, as they broadly cover two main scenarios of this problem.

One aspect of the problem is addressed by a great solution provided by Stefan Pochmann. So as mentioned before, it's quite possible that we have a gigantic matrix with a very few live cells. In that case it would be stupidity to save the entire board as is.

If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells.

Let's look at the sample code provided by Stefan for handling this aspect of the problem.

Essentially, we obtain only the live cells from the entire board and then apply the different rules using only the live cells and finally we update the board in-place. The only problem with this solution would be when the entire board cannot fit into memory. If that is indeed the case, then we would have to approach this problem in a different way. For that scenario, we assume that the contents of the matrix are stored in a file, one row at a time.

In order for us to update a particular cell, we only have to look at its 8 neighbors which essentially lie in the row above and below it. So, for updating the cells of a row, we just need the row above and the row below. Thus, we read one row at a time from the file and at max we will have 3 rows in memory. We will keep discarding rows that are processed and then we will keep reading new rows from the file, one at a time.'''
