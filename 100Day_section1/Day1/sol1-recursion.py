# This solution is not acceptable due to the running time exceeding
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def search(s, wordDict, left):
            if left >= len(s):
                return True
            
            for right in range(left+1, len(s)+1):
                if s[left:right] not in wordDict:
                    continue
                elif s[left:right] in wordDict and search(s, wordDict, right):
                    return True
            
            return False
        

        return search(s, wordDict, 0)