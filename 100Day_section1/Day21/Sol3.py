class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        self.ans = {}
        for n in range(len(nums)-1,-1,-1):
            if not self.ans:
                self.ans[nums[n]] = 1
                continue
            
            tmp_max = 0

            for key in self.ans.keys():
                if nums[n] < key:
                    tmp_max = max(tmp_max, self.ans[key])

            self.ans[nums[n]] = tmp_max + 1
        
        return max(self.ans.values())
