# Maximum Sum Subarray of Size K

## Problem Statement

Given an array of positive numbers and a positive number ‘k’, find the **maximum sum of any contiguous subarray of size ‘k’**.

### Example 1:

```markdown
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
```

### Example 2:

```markdown
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
```



## Solution:

Like what has been mentioned in the main idea, we use sliding window to solve this problem

```python
def max_sub_array_of_size_k(k, arr):
  _sum_avg = sum(arr[:k]) 
  max_avg = _sum_avg
  for idx in range(len(arr) - k - 1):
      _sum_avg = _sum_avg - arr[idx] + arr[idx+k]
      max_avg = max(max_avg, _sum_avg)
  return max_avg
```

