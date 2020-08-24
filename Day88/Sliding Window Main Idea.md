# Sliding Window Main Idea

## Question:

Given a list (for example [1, 3, 2, 6, -1, 4, 1, 8, 2]), return the average of K (K = 5) consecutive numbers in the list.

## Solution 1:

Brute Force solution:

```Python
def brute_force(arr, K):
    ans = []

    for idx in range(len(arr) - K + 1):
        tmp_ans = 0
        for r in range(idx, idx + K):
            tmp_ans += arr[r]
        
        ans.append(tmp_ans / K)

    return ans
```

The time complexity of this brute force solution is O(N*K) where N is the length of the array and K is the length of the sliding window

To optimize this solution, we can think about the sum in another way.

## Solution 2:

The difference of two consecutive sum is from the poping number and the pushing number:

  [1, 3, 2, 6, -1]

​      [3, 2, 6, -1, 4]

So basically, we can subtract the poping number from sum and add pushing number to quickly get the result

```python
def better_solution(arr, K):
    _sum = sum(arr[:K])
    ans = [_sum / K]

    for idx in range(1,len(arr) - K + 1):
        _sum = _sum - arr[idx - 1] + arr[idx + K - 1]
        ans.append(_sum / K)
    
    return ans
```

