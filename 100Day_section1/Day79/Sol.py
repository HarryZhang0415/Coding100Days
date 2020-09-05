class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def row_index(idx):
            if idx == 0:
                return [1]
            if idx == 1:
                return [1,1]
            
            ans = []
            
            l = row_index(idx - 1)
            
            for i in range(1,len(l)):
                ans.append(l[i-1] + l[i])
            
            return [1] + ans + [1]
        
        return row_index(rowIndex)