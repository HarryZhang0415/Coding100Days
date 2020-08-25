# Remove Duplicates

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/mEEA22L5mNA#problem-statement)

Given an array of sorted numbers, **remove all duplicates** from it. You should **not use any extra space**; after removing the duplicates in-place return the new length of the array.

**Example 1:**

```
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
```

**Example 2:**

```
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
```



 Solution 1: cut the array

```python
def remove_duplicates(arr):
  # TODO: Write your code here
  start = 0
  end = 1

  if len(arr) == 1:
    return 1
  elif arr[start] == arr[end] and len(arr) == 2:
    return 1
  else:
    while end < len(arr):
      if arr[start] == arr[end]:
        arr = arr[:end] + arr[end+1:]
      else:
        start += 1
        end += 1
    
    return len(arr)
  return -1

```

Solution 2: switch two numbers

In this problem, we need to remove the duplicates in-place such that the resultant length of the array remains sorted. As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we encounter duplicates. In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number. So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.

```python
def remove_duplicates(arr):
  # If we find the duplicate number, we need to make a switch of the numbers in the array
  # for example, [1,1,2,3], we need to switch the position of the second 1 and 2 first and then
  # make a switch of 1,3.
  switch_left = 1 # remember the position of left switch number
  
  for switch_right in range(1, len(arr)):
    if arr[switch_left - 1] != arr[switch_right]: 
        # here switch_left - 1 means the previous number
        # the first time we made a switch, the array turns into [1,2,1,3] and switch_left points to the position of the second 1 now and point_right points to the position of 3. 
        # However, rather than comparing 1 and 3, we now need to compare 2 and 3 but the position of 2 is point_left - 1 instead of point_left. That's the reason why we use switch_left - 1 to make the comparison.
      arr[switch_left] = arr[switch_right]
      switch_left += 1

  return switch_left

```

