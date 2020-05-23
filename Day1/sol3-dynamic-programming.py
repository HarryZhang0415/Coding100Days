'''
Approach 4: Using Dynamic Programming
https://leetcode.com/articles/word-break/
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for i in range(len(s)+1)]
        memo[0] = True

        for i in range(1,len(s)+1):
            for j in range(i):
                if memo[j] and s[j:i] in wordDict:
                    memo[i] = True
                    break
        
        return memo[len(s)]