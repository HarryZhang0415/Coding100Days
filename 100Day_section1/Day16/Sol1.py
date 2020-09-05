# sort the string and compare. Not accepted, time exceeding.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        self.ans = []
        start = 0
        
        while start < len(s):
            if sorted(s[start:start+len(p)]) == sorted(p):
                self.ans.append(start)

            start += 1

        return self.ans