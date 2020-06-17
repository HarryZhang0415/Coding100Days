# Time limit exceeds --> not accepted

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.end = [m-1, n-1]
        self.start = [0, 0]
        
        self.ans = []

        def search(row, col, end, tmp_list):
            if end[0] == row and end[1] == col:
                self.ans.append(tmp_list)
                return
                
            tmp_list.append([row, col])
            
            if row < end[0]:
                search(row + 1, col, end, tmp_list)
            if col < end[1]:
                search(row, col + 1, end, tmp_list)
        
        search(self.start[0], self.start[1], self.end, [])

        return len(self.ans)