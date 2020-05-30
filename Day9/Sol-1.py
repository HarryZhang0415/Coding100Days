'''
Approach 1: Heap
Let's start from the simple heap approach with \mathcal{O}(N \log k)O(Nlogk) time complexity. To ensure that \mathcal{O}(N \log k)O(Nlogk) is always less than \mathcal{O}(N \log N)O(NlogN), the particular case k = Nk=N could be considered separately and solved in \mathcal{O}(N)O(N) time.

Algorithm

The first step is to build a hash map element -> its frequency. In Java, we use the data structure HashMap. Python provides dictionary subclass Counter to initialize the hash map we need directly from the input array.
This step takes \mathcal{O}(N)O(N) time where N is a number of elements in the list.

The second step is to build a heap of size k using N elements. To add the first k elements takes a linear time \mathcal{O}(k)O(k) in the average case, and \mathcal{O}(\log 1 + \log 2 + ... + \log k) = \mathcal{O}(log k!) = \mathcal{O}(k \log k)O(log1+log2+...+logk)=O(logk!)=O(klogk) in the worst case. It's equivalent to heapify implementation in Python. After the first k elements we start to push and pop at each step, N - k steps in total. The time complexity of heap push/pop is \mathcal{O}(\log k)O(logk) and we do it N - k times that means \mathcal{O}((N - k)\log k)O((N−k)logk) time complexity. Adding both parts up, we get \mathcal{O}(N \log k)O(Nlogk) time complexity for the second step.

The third and the last step is to convert the heap into an output array. That could be done in \mathcal{O}(k \log k)O(klogk) time.

In Python, library heapq provides a method nlargest, which combines the last two steps under the hood and has the same \mathcal{O}(N \log k)O(Nlogk) time complexity.
'''

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k): 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 