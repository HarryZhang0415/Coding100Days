# Problem Challenge 1

### Permutation in a String (hard) [#](https://www.educative.io/courses/grokking-the-coding-interview/N8vB7OVYo2D#permutation-in-a-string-hard)

Given a string and a pattern, find out if the **string contains any permutation of the pattern**.

**Permutation** is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

If a string has ‘n’ distinct characters it will have n!*n*! permutations.

**Example 1:**

```
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
```

**Example 2:**

```
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
```

**Example 3:**

```
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
```

**Example 4:**

```
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
```



Solution 1: Using Python internal dictionary.

```python
def find_permutation(str, pattern):
  # TODO: Write your code here
  dic = {}
  for letter in pattern:
    if letter not in dic.keys():
      dic[letter] = 1
    else:
      dic[letter] += 1
  
  tmp_dic = {}

  for idx in range(len(pattern)):
    if str[idx] not in tmp_dic:
      tmp_dic[str[idx]] = 1
    else:
      tmp_dic[str[idx]] += 1
  
  if tmp_dic == dic:
    return True

  for idx in range(len(str) - len(pattern)):
    if tmp_dic[str[idx]] > 1:
      tmp_dic[str[idx]] -= 1
    else:
      del(tmp_dic[str[idx]])
    
    if str[idx + len(pattern)] not in tmp_dic.keys():
      tmp_dic[str[idx + len(pattern)]] = 1
    else:
      tmp_dic[str[idx + len(pattern)]] += 1
    
    if tmp_dic == dic:
      return True
  
  return False

```

Time complexity is O(N*K). Here N is the length of the string and K is the distinct value in the string

Solution 2: Official Solution:

1. Create a **HashMap** to calculate the frequencies of all characters in the pattern.
2. Iterate through the string, adding one character at a time in the sliding window.
3. If the character being added matches a character in the **HashMap**, decrement its frequency in the map. If the character frequency becomes zero, we got a complete match.
4. If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the **HashMap**), we have gotten our required permutation.
5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the size of the pattern. At the same time, if the character going out was part of the pattern, put it back in the frequency **HashMap**.

```python
def find_permutation(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()

```

