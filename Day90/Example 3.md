# Squaring a Sorted Array

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/R1ppNG3nV9R#problem-statement)

Given a sorted array, create a new array containing **squares of all the number of the input array** in the sorted order.

**Example 1:**

```
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
```

**Example 2:**

```
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
```



### Solution [#](https://www.educative.io/courses/grokking-the-coding-interview/R1ppNG3nV9R#solution)

This is a straightforward question. The only trick is that we can have negative numbers in the input array, which will make it a bit difficult to generate the output array with squares in sorted order.

An easier approach could be to first find the index of the first non-negative number in the array. After that, we can use **Two Pointers** to iterate the array. One pointer will move forward to iterate the non-negative numbers and the other pointer will move backward to iterate the negative numbers. At any step, whichever number gives us a bigger square will be added to the output array. 

Since the numbers at both the ends can give us the largest square, an alternate approach could be to use two pointers starting at both the ends of the input array. At any step, whichever pointer gives us the bigger square we add it to the result array and move to the next/previous number according to the pointer. 

```python
def make_squares(arr):
  squares = []
  # TODO: Write your code here
  left = 0
  right = len(arr) - 1

  while left <= right:
    left_square = arr[left] ** 2
    right_square = arr[right] ** 2
    if left_square < right_square:
      squares.insert(0,right_square)
      right -= 1
    else:
      squares.insert(0,left_square)
      left += 1
      
  return squares

```

