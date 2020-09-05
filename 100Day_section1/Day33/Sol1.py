# Enumerate all the path and find the two list which merge together as nums --> failed because of time limit exceeding

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        self.ans = []
        
        if sum(nums) % 2 != 0:
            return False
        elif sum(nums) / 2 < max(nums):
            return False
        else:
            self.search(nums, 0, [], sum(nums) / 2)
            for n1 in range(len(self.ans)):
                for n2 in range(n1+1, len(self.ans)):
                    if sorted(self.ans[n1] + self.ans[n2]) == nums:
                        return True
            
            return False
    
    def search(self, nums, idx, tmp_list, target):
        if sum(tmp_list) == target:
            self.ans.append(tmp_list)
            return
        if idx >= len(nums):
            return
        if sum(tmp_list) > target:
            return
        
        self.search(nums, idx+1, tmp_list +[nums[idx]], target)
        self.search(nums, idx+1, tmp_list, target)
        