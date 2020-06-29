class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort = sorted(nums)
        
        start = 0
        
        while start < len(nums) and sort[start] == nums[start]:
            start += 1
        
        if start == len(nums):
            return 0
        
        end = len(sort) - 1
        
        while sort[end] == nums[end]:
            end -= 1
        
        return end - start + 1