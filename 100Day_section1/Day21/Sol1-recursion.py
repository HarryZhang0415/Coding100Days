# Simple recursion, time complexity --> 2^n  not accepted, time exceeding
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def search(nums, prev, idx):
            if idx >= len(nums):
                return 0
            
            taken = 0
            if nums[idx] > prev:
                taken = 1 + search(nums, nums[idx], idx + 1)
            
            nottaken = search(nums, prev, idx + 1)
            return max(taken, nottaken)
        
        return search(nums, float('-inf'), 0)
                