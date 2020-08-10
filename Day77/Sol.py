class Solution:
    def titleToNumber(self, s: str) -> int:
        dic = {chr(i):i-64 for i in range(65,91)}
        
        if len(s) == 1:
            return dic[s]
        
        ans = 0
        
        while s:
            curr = s[0]
            s = s[1:]
            
            ans += dic[curr] * (26**len(s))
        
        return ans