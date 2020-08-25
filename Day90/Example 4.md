# Triplet Sum to Zero

### Problem Statement [#](https://www.educative.io/courses/grokking-the-coding-interview/gxk639mrr5r#problem-statement)

Given an array of unsorted numbers, find all **unique triplets in it that add up to zero**.

**Example 1:**

```
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
```

**Example 2:**

```
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
```



### Solution [#](https://www.educative.io/courses/grokking-the-coding-interview/gxk639mrr5r#solution)

This problem follows the **Two Pointers** pattern and shares similarities with [Pair with Target Sum](https://www.educative.io/collection/page/5668639101419520/5671464854355968/6618310940557312/). A couple of differences are that the input array is not sorted and instead of a pair we need to find triplets with a target sum of zero.

To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X + Y + Z == 0*X*+*Y*+*Z*==0. At this stage, our problem translates into finding a pair whose sum is equal to “-X−*X*” (as from the above equation Y + Z == -X*Y*+*Z*==−*X*).

Another difference from [Pair with Target Sum](https://www.educative.io/collection/page/5668639101419520/5671464854355968/6618310940557312/) is that we need to find all the unique triplets. To handle this, we have to skip any duplicate number. Since we will be sorting the array, so all the duplicate numbers will be next to each other and are easier to skip.

```python
def search_triplets(arr):
  triplets = []
  # TODO: Write your code here
  arr.sort()
  for idx in range(len(arr)):
    left = idx + 1
    triplets = search_tri(arr, -arr[idx], left, triplets)

  return triplets

def search_tri(arr, target, left, triplets):
  start = left
  end = len(arr) - 1

  while start <= end:
    if arr[start] + arr[end] == target:
      triplets.append([-target, arr[start], arr[end]])
      start += 1
      end -= 1
    elif arr[start] + arr[end] < target:
      start += 1
    else:
      end -= 1
  
  return triplets
```

