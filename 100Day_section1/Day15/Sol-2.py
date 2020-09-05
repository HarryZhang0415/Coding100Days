'''
Solution

Maximum Product Subarray https://leetcode.com/problems/maximum-product-subarray/?tab=Description

https://www.quora.com/How-do-I-solve-maximum-product-subarray-problems
Use an example: [2,-3,4,-8,0]
Insights:
What if the array has just positive numbers including zero?
A solution of this will maintain max_prod[i] where max_prod[i] is the maximum subarray product ending at i. Then max_prod[i+1] = max(max_prod[i] * nums[i+1], nums[i+1]).
Now how do we change the solution when we allow negative numbers?
Imagine that we have both max_prod[i] and min_prod[i] i.e. max prod ending at i and min prod ending at i. Now if we have a negative number at nums[i+1] and if min_prod[i] is negative, then the product of the two will be positive and can potentially be largest product. Key point is to maintain both max_prod and min_prod such that at iteration i, they refer to the max and min prod ending at index i -1.
You have three choices to make at any position in array.

You can get maximum product by multiplying the current element with
1. maximum product calculated so far. (might work when currentelement is positive).

2. You can get maximum product by multiplying the current element with minimum product calculated so far. (might work when current element is negative).

3. Current element might be a starting position for maximum product subarray
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max = nums[0]
        Min = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            tmp_Max = max(nums[i], Max * nums[i], Min * nums[i])
            tmp_Min = min(nums[i], Max * nums[i], Min * nums[i])
            
            ## Every time do all the calculation first and then update Max and Min value
            
            Max, Min = tmp_Max, tmp_Min
            
            ans = max(Max, ans)
        
        return ans