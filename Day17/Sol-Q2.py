## Approach link: https://leetcode.com/problems/decode-ways/solution/

class Solution:
    def __init__(self):
        self.memo = {}

    def recursive_with_memo(self, index, s):
        # If reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1
        
        # If the string starts with a zero, it can not be decoded
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1
        
        if index in self.memo:
            return self.memo[index]

        ans = self.recursive_with_memo(index+1, s) \
            + (self.recursive_with_memo(index+2, s) if (int(s[index:index+1]) <= 26) else 0)

        # Save for memoization
        self.memo[index] = ans

        return ans
    
    def numDecoding(self, s):
        if not s:
            return 0
        return self.recursive_with_memo(0,s)