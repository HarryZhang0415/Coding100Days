#Cases passed, time excceeding --> not accepted
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        self.memo = []
        
        def pala(s):
            if s in self.memo:
                return True
            
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            self.memo.append(s)
            return True
        
        idx = 0
        for l in range(len(s)):
            for j in range(l+1, len(s)+1):
                if pala(s[l:j]):
                    self.ans += 1
        
        return self.ans
            
        