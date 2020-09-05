'''
The core idea here is to think about the dynamic programming.
https://leetcode.com/problems/decode-ways/solution/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0 for i in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for idx in range(2, len(dp)):
            if s[idx - 1] != '0':
                dp[idx] += dp[idx - 1]
            
            two_word = int(s[idx-2:idx])

            if two_word >= 10 and two_word <= 26:
                dp[idx] += dp[idx - 2]
        
        return dp[len(s)]

