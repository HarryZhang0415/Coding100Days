# 贪心算法
# we need "last" to store the last position appeared of each letter. Then we use start and end to record for loop situation.
class Solution(object):
    def partitionLabels(self, S):
        last = {letter:number for number,letter in enumerate(S)}
        
        start = end = 0
        ans = []
        
        for number, letter in enumerate(S):
            end = max(end, last[letter])
            
            if number == end:
                ans.append(end-start+1)
                start = number + 1
        
        return ans