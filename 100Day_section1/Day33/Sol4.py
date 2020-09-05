# Resursion with memo  --> not accepted due to time exceeding
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.ans = False
        target = sum(nums)
        
        def search(idx, nums, tmp_list, target):
            if sum(tmp_list) == target / 2:
                self.ans = True
                return
            if self.ans:
                return
            if idx >= len(nums):
                return
            
            search(idx + 1, nums, tmp_list + [nums[idx]], target)
            search(idx + 1, nums, tmp_list, target)
        
        if target % 2 != 0:
            return False
        elif target / 2 < max(nums):
            return False
        else:
            search(0, nums, [], target)
            return self.ans