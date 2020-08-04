### 注意是alphanumeric 而不是单纯的alpha或者numeric

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        s = s.replace(' ','')
        s = s.lower()
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                left += 1
                right -= 1
        
        return True