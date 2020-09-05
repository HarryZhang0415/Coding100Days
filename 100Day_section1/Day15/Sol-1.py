# Recursion --> time exceeds, not accepted

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.Max = float('-inf')
        
        def search(nums, idx, tmp_mult):
            if idx >= len(nums):
                return
            
            self.Max = max(self.Max, tmp_mult * nums[idx], nums[idx])
            
            search(nums, idx+1, tmp_mult * nums[idx])
            search(nums, idx+1, nums[idx])
        
        search(nums, 0, 1)
        return self.Max