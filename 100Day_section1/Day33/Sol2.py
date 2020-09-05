# Recursion --> time limit exceeding

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        self.ans = []
        
        if sum(nums) % 2 != 0:
            return False
        elif sum(nums) / 2 < max(nums):
            return False
        else:
            return self.search([],[],0,nums)
    
    
    def search(self, left , right, idx, nums):
        if sum(left) == sum(right) and sum(left) == sum(nums) / 2:
            return True
        if idx >= len(nums):
            return False
        
        return (self.search(left + [nums[idx]], right, idx + 1, nums) or 
               self.search(left, right + [nums[idx]], idx + 1, nums) )
        
    
