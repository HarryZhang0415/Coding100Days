from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = Counter(nums)
        tmp = []
        
        for key in range(3):
            for n in range(ans[key]):
                tmp += [key]
        
        
        for i in range(len(nums)):
            nums[i] = tmp[i]