class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        self.d = {}
        for n in nums:
            if n not in self.d:
                self.d[n] = 1
            else:
                return n