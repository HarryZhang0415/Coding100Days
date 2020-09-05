class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        ans = []
        
        point_a, point_b = 0,0
        
        while point_a < len(A) and point_b < len(B):
            if A[point_a][1] < B[point_b][0]: 
                point_a += 1
                continue
            elif A[point_a][0] > B[point_b][1]:
                point_b += 1
                continue
                
            left = max(A[point_a][0], B[point_b][0])
            right = min(A[point_a][1], B[point_b][1])
            
            ans.append([left, right])
            
            if A[point_a][1] < B[point_b][1]:  ### 用尾端进行比较可以避免 [9,20] vs [9,10],[11,12]这样的情况
                point_a += 1
            else:
                point_b += 1
        
        return ans