class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        
        dic = collections.defaultdict(int)
        for char in s:
            dic[char] += 1
        
        ans = 0
        has_one = False
        
        for k,v in dic.items():
            if v % 2 == 1:
                has_one = True
                ans += (v - 1)
            if v % 2 == 0:
                ans += v
        
        return ans + has_one
            
            