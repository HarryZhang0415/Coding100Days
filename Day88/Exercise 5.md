# No-repeat Substring

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO#problem-statement)

Given a string, find the **length of the longest substring** which has **no repeating characters**.

**Example 1:**

```
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
```

**Example 2:**

```
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
```

**Example 3:**

```
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
```



## Solution:

This problem follows the **Sliding Window** pattern and we can use a similar dynamic sliding window strategy as discussed in [Longest Substring with K Distinct Characters](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5698217712812032/). We can use a **HashMap** to remember the last index of each character we have processed. Whenever we get a repeating character we will shrink our sliding window to ensure that we always have distinct characters in the sliding window.

```
def non_repeat_substring(str):
  # TODO: Write your code here
  start = 0
  max_length = 0
  tmp_ans = ''

  dic = {}

  for end in range(len(str)):
    tmp_ans += str[end]
    if str[end] not in dic.keys():
      dic[str[end]] = 1
    else:
      max_length = max(max_length, end - start)
      dic[str[end]] += 1
      while dic[str[end]] > 1:
        tmp_ans = tmp_ans[1:]
        del_letter = str[start]
        if dic[del_letter] > 1:
          dic[del_letter] -= 1
        else:
          del(dic[del_letter])
        start += 1
  
  max_length = max(max_length, len(tmp_ans))

  return max_length
```

