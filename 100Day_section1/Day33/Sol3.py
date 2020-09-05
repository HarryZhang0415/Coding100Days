# Dynamic programming

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (sum(nums) / 2.)  in possible_sums  