## Solution 1: Recursion --> not accepted, time exceeding

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        self.dp = [0 for i in range(len(T))]
        def search(T, idx, com):
            if idx < 0: return
            elif idx == len(T) - 1 or com >= len(T):
                self.dp[idx] = 0
                
            
            elif T[idx] < T[com]:
                self.dp[idx] = com - idx
                
                
            elif T[idx] >= T[com]:
                search(T, idx, com + 1)
            
            search(T, idx - 1, idx)
        
        search(T, len(T) - 1, len(T) - 1)
        return self.dp

## Solution 2:
## Using Stack to delete downtrend  https://leetcode.com/problems/daily-temperatures/solution/
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for i in range(len(T))]
        
        stack = []
        
        for i in range(len(T)-1,-1,-1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
                
        return ans