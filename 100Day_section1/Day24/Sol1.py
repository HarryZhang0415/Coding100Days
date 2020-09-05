# Recursion with memoization --> Time limit exceed, not accepted

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        self.path = [False] * len(nums)
        
        def search(nums, index):
            if index >= len(nums):
                return 
            if self.path[-1]:
                return
            
            self.path[index] = True
            
            if nums[index] == 0:
                return
            
            for i in range(nums[index], 0,-1):
                search(nums, index + i)
                
        search(nums, 0)
        
        return self.path[len(nums) - 1]
                
                