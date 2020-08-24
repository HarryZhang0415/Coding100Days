# Problem Challenge 2

### String Anagrams (hard) [#](https://www.educative.io/courses/grokking-the-coding-interview/YQ8N2OZq0VM#string-anagrams-hard)

Given a string and a pattern, find **all anagrams of the pattern in the given string**.

**Anagram** is actually a **Permutation** of a string. For example, “abc” has the following six anagrams:

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

**Example 1:**

```
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
```

**Example 2:**

```
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
```



Solution 1:

```python
def find_string_anagrams(str, pattern):
  result_indexes = []
  # TODO: Write your code here
  dic = {}

  tmp_dic = {}

  for idx in range(len(pattern)):
    if pattern[idx] not in dic:
      dic[pattern[idx]] = 1
    else:
      dic[pattern[idx]] += 1

    if str[idx] not in tmp_dic:
      tmp_dic[str[idx]] = 1
    else:
      tmp_dic[str[idx]] += 1
  
  if tmp_dic == dic:
    result_indexes += [i for i in range(len(pattern))]
    return result_indexes

  for idx in range(len(str) - len(pattern)):
    tmp_dic[str[idx]] -= 1
    if str[idx + len(pattern)] not in tmp_dic.keys():
      tmp_dic[str[idx + len(pattern)]] = 1
    else:
      tmp_dic[str[idx + len(pattern)]] += 1
    
    if tmp_dic == dic:
      result_indexes += [i for i in range(idx + 1, idx + len(pattern) + 1)]
      return result_indexes

  return result_indexes
```

