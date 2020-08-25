# Triplet Sum Close to Target

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/3YlQz7PE7OA#problem-statement)

Given an array of unsorted numbers and a target number, find a **triplet in the array whose sum is as close to the target number as possible**, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

**Example 1:**

```
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
```

**Example 2:**

```
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
```

**Example 3:**

```
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
```



### Solution [#](https://www.educative.io/courses/grokking-the-coding-interview/3YlQz7PE7OA#solution)

This problem follows the **Two Pointers** pattern and is quite similar to [Triplet Sum to Zero](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5679549973004288/).

We can follow a similar approach to iterate through the array, taking one number at a time. At every step, we will save the difference between the triplet and the target number, so that in the end, we can return the triplet with the closest sum.

```python
import math
def triplet_sum_close_to_target(arr, target_sum):
  # TODO: Write your code here

  arr.sort()

  diff = math.inf
  ans = math.inf

  for idx in range(len(arr)):
    left = idx + 1
    diff, ans = search_tri(arr, arr[idx], left, target_sum, diff, ans)
  return ans

def search_tri(arr, n1, left, target_sum, diff, ans):
  start = left
  end = len(arr) - 1

  while start < end:
    tmp_sum = n1 + arr[start] + arr[end]
    tmp_diff = abs(target_sum - tmp_sum)
    if tmp_diff < diff:
      ans = tmp_sum
      diff = tmp_diff
    elif tmp_diff == diff:
      ans = min(ans, tmp_sum)
    if tmp_sum < target_sum:
      start += 1
    else:
      end -= 1
  
  return (diff, ans)
```

