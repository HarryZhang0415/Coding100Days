# Subarrays with Product Less than a Target

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/RMV1GV1yPYz#problem-statement)

Given an array with positive numbers and a target number, find all of its contiguous subarrays whose **product is less than the target number**.

**Example 1:**

```
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
```

**Example 2:**

```
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
```



### Solution [#](https://www.educative.io/courses/grokking-the-coding-interview/RMV1GV1yPYz#solution)

This problem follows the **Sliding Window** and the **Two Pointers** pattern and shares similarities with [Triplets with Smaller Sum](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5554621957275648/) with two differences:

1. In this problem, the input array is not sorted.
2. Instead of finding triplets with sum less than a target, we need to find all subarrays having a product less than the target.

The implementation will be quite similar to [Triplets with Smaller Sum](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5554621957275648/).

```python
from collections import deque

def find_subarrays(arr, target):
  result = []
  # TODO: Write your code here
  start = 0
  tmp_mult = 1

  for end in range(len(arr)):
    tmp_mult *= arr[end]

    while tmp_mult >= target:
      tmp_mult /= arr[start]
      start += 1
    
    tmp_ans = deque()
    for idx in range(end, start - 1, -1):
      tmp_ans.insert(0,arr[idx])
      result.append(list(tmp_ans))

  return result

```

