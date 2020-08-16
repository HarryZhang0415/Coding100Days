# Series: best time to buy and sell stocks I

q1:

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Answer:

Since we are only permitted to complete at most one transaction, the basic idea is to remember the min and max of the list.
For the process in a loop, we use p to represent the current price, ans to store the result and maximum, minimum to store the edges.

If current price p is less than minimum, this means taht we have a new valley, we change minimum to this value and dont change the price.
For other situation, we change the ans.

code:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        ans = 0
        
        for p in prices:
            if p < minimum:
                minimum = p
                continue
            ans = max(ans, p - minimum)
        
        return ans
            
# Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

solution:
## Solution 1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dic = collections.defaultdict(int) # this helps to record the max profit before price p
        
        minimum = float('inf')  # initialize the minimum as max
        ans = 0 # initial the profit as 0
        
        for p in prices:
            if p <= minimum:    
            # In an decreasing order, the max profit before current price is the same as the previous 1 price. For example, 1 7 6 5 4 3 2, the max profit for 6 5 4 3 2 is the same as 7, which 
            # is 6
                dic[p] = ans
                minimum = p
                continue
            else:
            # for other situation, we do a loop for previous all numbers. The curretn profit is: current price - previous price + the max profit before previous price(stored in the hashmap)
                for key in dic.keys():
                    if p >= key:
                        ans = max(ans, dic[key] + p - key) 
                    else:
                        continue
                dic[p] = ans
        
        return max(dic.values())

## Solution 2: Peak Valley approach from https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        valley = prices[0]
        peak = prices[0]
        
        ans = 0
        
        idx = 0
        
        while idx < len(prices) - 1:
            while idx < len(prices) - 1 and prices[idx] >= prices[idx + 1]:
                idx += 1
            valley = prices[idx]
            
            while idx < len(prices) - 1 and prices[idx] <= prices[idx + 1]:
                idx += 1
            peak = prices[idx]
            
            ans += peak - valley
        
        return ans

