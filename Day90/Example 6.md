# Triplets with Smaller Sum

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/mElknO5OKBO#problem-statement)

Given an array `arr` of unsorted numbers and a target sum, **count all triplets** in it such that **`arr[i] + arr[j] + arr[k] < target`** where `i`, `j`, and `k` are three different indices. Write a function to return the count of such triplets.

**Example 1:**

```
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
```

**Example 2:**

```
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
```



### Solution [#](https://www.educative.io/courses/grokking-the-coding-interview/mElknO5OKBO#solution)

This problem follows the **Two Pointers** pattern and shares similarities with [Triplet Sum to Zero](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5679549973004288/). The only difference is that, in this problem, we need to find the triplets whose sum is less than the given target. To meet the condition `i != j != k` we need to make sure that each number is not used more than once.

Following a similar approach, first, we can sort the array and then iterate through it, taking one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X + Y + Z < target*X*+*Y*+*Z*<*t**a**r**g**e**t*. At this stage, our problem translates into finding a pair whose sum is less than “target - X*t**a**r**g**e**t*−*X*” (as from the above equation Y + Z == target - X*Y*+*Z*==*t**a**r**g**e**t*−*X*). We can use a similar approach as discussed in [Triplet Sum to Zero](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5679549973004288/).

```python
def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()
  # TODO: Write your code here
  for idx in range(len(arr)):
    left = idx + 1
    count = search_tri(arr, arr[idx], left, count, target)
  return count

def search_tri(arr, n1, left, count, target):
  start = left 
  end = len(arr) - 1 
  while start < end:
    tmp_sum = n1 + arr[start] + arr[end]
    if tmp_sum < target:
      count += end - start  ######### this is the difference
      start += 1
    else:
      end -= 1
  
  return count
```

