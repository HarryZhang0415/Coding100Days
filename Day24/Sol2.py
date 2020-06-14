## loop with only detect 0 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def backtrack(nums, index, curr):
            if curr < 0:
                return False
            
            max_step = nums[curr]
            if curr + max_step > index:
                return True
            else:
                return backtrack(nums, index, curr - 1)
        
        if len(nums) == 1:
            return True
        
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                if not backtrack(nums, i, i-1):
                    return False
            
        return True