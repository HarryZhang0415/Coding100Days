class Solution:
    def validPalindrome(self, s: str) -> bool:
        def search(i, j):
            return all([s[k] == s[j-k+i] for k in range(i,j)])

        for idx in range(len(s)):
            if s[idx] != s[~idx]:
                j = len(s) - 1 - idx
                return search(idx+1,j) or search(idx,j-1)
        return True

        

class Solution(object):
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True