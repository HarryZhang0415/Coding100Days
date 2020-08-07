# Hashmap time complexity O(n) space complexity O(n)

# Using negative value for storing whether visited or not
# https://leetcode.com/problems/find-all-duplicates-in-an-array/solution/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for n in nums:
            idx = abs(n) - 1
            number = nums[idx]
            
            if number < 0:
                ans.append(abs(n))
            else:
                nums[idx] = - number
        
        return ans