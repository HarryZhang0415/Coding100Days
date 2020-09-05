from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []       
       
        sCounter = Counter(s[:len(p)])
        pCounter = Counter(p)
        
        self.ans = []
        start = 0
        
        if sCounter == pCounter:
            self.ans.append(0)

        while start < len(s) - len(p):
            pop_item = s[start]
            push_item = s[start+len(p)]

            sCounter[pop_item] -= 1      
            ### If the item in the dictionary is 0, we should delete the item instead of leaving it there in order to match the dictionaries.
            if sCounter[pop_item] == 0:
                del sCounter[pop_item]
                
            sCounter[push_item] += 1

            start += 1

            if sCounter == pCounter:
                self.ans.append(start)


        return self.ans