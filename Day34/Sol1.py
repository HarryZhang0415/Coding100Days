## Brute Force --> not accepted due to time exceeds

class Solution:
    def numSquares(self, n: int) -> int:
        idx = 1
        self.nums = []
        while idx ** 2 <= n:
            self.nums.append(idx ** 2)
            idx += 1
        
        self.nums.sort(reverse=True)
        self.ans = float('inf')
        
        def search(tmp_list, target, idx, nums):
            if sum(tmp_list) == target:
                self.ans = min(self.ans, len(tmp_list))
                return
            
            if idx >= len(nums) or sum(tmp_list) > target:
                return
            
            search(tmp_list,  target, idx+1, nums)
            search(tmp_list + [nums[idx]],  target, idx, nums)
            search(tmp_list + [nums[idx]],  target, idx + 1, nums)
        
        search([], n, 0, self.nums)
        
        return self.ans 