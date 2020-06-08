# Recursion --> Accepted

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        
        def recursion(nums, tmp_list, idx):
            
            if tmp_list not in self.ans:
                self.ans.append(tmp_list)
            if idx >= len(nums):
                return
           
            recursion(nums, tmp_list, idx + 1)
            recursion(nums, tmp_list + [nums[idx]], idx + 1)
         
        recursion(nums, [], 0)
        return self.ans