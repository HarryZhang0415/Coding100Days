# This approach use recursion with memory. The results of previous paths walked were stored in the memo
# When new situation comes in, it search the previous result and return. 
# Accepted

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def search(s, wordDict, left, memo):
            if left >= len(s):
                return True
            
            if left in memo.keys():
                return memo[left]
            
            for right in range(left+1, len(s) + 1):
                if s[left: right] not in wordDict:
                    continue
                elif s[left:right] in wordDict and search(s, wordDict, right, memo):
                    memo[left] = True
                    return True
                
            memo[left] = False
            return False
        
        return search(s, wordDict, 0, {})