# Dutch National Flag Problem

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/RMBxV6jz6Q0#problem-statement)

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called [Dutch National Flag problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem).

**Example 1:**

```
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
```

**Example 2:**

```
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
```



### Solution [#](https://www.educative.io/courses/grokking-the-coding-interview/RMBxV6jz6Q0#solution)

The brute force solution will be to use an in-place sorting algorithm like [Heapsort](https://en.wikipedia.org/wiki/Heapsort) which will take O(N*logN)*O*(*N*∗*l**o**g**N*). Can we do better than this? Is it possible to sort the array in one iteration?

We can use a **Two Pointers** approach while iterating through the array. Let’s say the two pointers are called `low` and `high` which are pointing to the first and the last element of the array respectively. So while iterating, we will move all 0s before `low` and all 2s after `high` so that in the end, all 1s will be between `low` and `high`.

```python
def dutch_flag_sort(arr):
  # TODO: Write your code here
  left = 0
  right = len(arr) - 1
  idx = 0

  while idx <= right:
    if arr[idx] == 0:
      arr[idx], arr[left] = arr[left], arr[idx]
      idx += 1
      left += 1
    elif arr[idx] == 1:
      idx += 1
    else:
      arr[idx], arr[right] = arr[right], arr[idx]
      right -= 1
```

