# 131. Palindrome Partitioning

## Description:
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

## Solution:

思路：因为这道题还是比较复杂的，所以最直观的方法就是枚举。列出所有可能性，将所有结果存储到ans里面并返回。

function description:

partition: main function for using other functions, the function which returns the final result

dfs: listing every possible solution and testing them.

ispal: testing whether one subsequence is parlindrome or not

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = [] ## this store the final result
        self.dfs(s, []) ## there are two parameters for this function, one is the string and the other is the possible path

        return self.ans
    
    def dfs(self, s, path):
        if not s: ## which means the algo goes to the end
            self.ans.append(path)
            return
        
        else:
            for i in range(1, len(s) + 1):
                if self.ispal(s[:i]):
                    self.dfs(s[i:], path + [s[:i]])

    def ispal(self, s):
        return s == s[::-1]

Since this method requires to go through all the possible solutions, the worst case for this is that there could be 2^N subsets and for each substring it takes O(N) time to generate substring and determine if it is a parlindrome or not.
