# 705. Design HashSet  Solution: https://leetcode.com/articles/design-hashset/

'''Solution
Intuition
This is a classical question from textbook, which is intended to test one's knowledge on data structure. Therefore, needless to say, it is not desirable to solve the problem with any build-in HashSet data structure.

There are two key questions that one should address, in order to implement the HashSet data structure, namely hash function and collision handling.

hash function: the goal of the hash function is to assign an address to store a given value. Ideally, each unique value should have an unique hash value.

collision handling: since the nature of a hash function is to map a value from a space A into a corresponding value in a smaller space B, it could happen that multiple values from space A might be mapped to the same value in space B. This is what we call collision. Therefore, it is indispensible for us to have a strategy to handle the collision.

Overall, there are several strategy to resolve the collisions:

Separate Chaining: for values with the same hash key, we keep them in a bucket, and each bucket is independent from each other.

Open Addressing: whenever there is a collision, we keep on probing on the main space with certain strategy until a free slot is found.

2-Choice Hashing: we use two hash functions rather than one, and we pick the generated address with fewer collision.

In this article, we focus on the strategy of separate chaining. Here is how it works overall.

Essentially, the primary storage underneath a HashSet is a continuous memory as Array. Each element in this array corresponds to a bucket that stores the actual values.

Given a value, first we generate a key for the value via the hash function. The generated key serves as the index to locate the bucket.

Once the bucket is located, we then perform the desired operations on the bucket, such as add, remove and contains.

Approach 1: LinkedList as Bucket
Intuition

The common choice of hash function is the modulo operator, i.e. \text{hash} = \text{value} \mod \text{base}hash=valuemodbase. Here, the \text{base}base of modulo operation would determine the number of buckets that we would have at the end in the HashSet.

Theoretically, the more buckets we have (hence the larger the space would be), the less likely that we would have collisions. The choice of \text{base}base is a tradeoff between the space and the collision.

In addition, it is generally advisable to use a prime number as the base of modulo, e.g. 769769, in order to reduce the potential collisions.

pic

As to the design of bucket, again there are several options. One could simply use another Array as bucket to store all the values. However, one drawback with the Array data structure is that it would take \mathcal{O}(N)O(N) time complexity to remove or insert an element, rather than the desired \mathcal{O}(1)O(1).

Since for any update operation, we would need to scan the entire bucket first to avoid any duplicate, a better choice for the implementation of bucket would be the LinkedList, which has a constant time complexity for the insertion as well as deletion, once we locate the position to update.

Algorithm

As we discussed in the above section, here we adopt the LinkedList to implement our bucket within the HashSet.

Essentially, we are implementing a LinkedList that does not contain any duplicate.

For each of the functions of add, remove and contains, we first generate the bucket index with the hash function. Then, we simply pass down the operation to the underlying bucket.'''


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

'''
Implementation Notes

In the Python implementation, we employed a sort of pseudo head to keep a reference to the actual head of the LinkedList, which could simplify a bit the logic by reducing the number of branchings.

For a value that was never seen before, we insert it to the head of the bucket, though we could also append it to the tail. It is a choice that we made, which could fit better the scenario where redundant values are operated in nearby time windows, since it is more likely that we spot the value at the head of the bucket rather than walking through the entire bucket.

Complexity Analysis

Time Complexity: \mathcal{O}(\frac{N}{K})O( 
K
N
​	
 ) where NN is the number of all possible values and KK is the number of predefined buckets, which is 769.

Assuming that the values are evenly distributed, thus we could consider that the average size of bucket is \frac{N}{K} 
K
N
​	
 .

Since for each operation, in the worst case, we would need to scan the entire bucket, hence the time complexity is \mathcal{O}(\frac{N}{K})O( 
K
N
​	
 ).

Space Complexity: \mathcal{O}(K+M)O(K+M) where KK is the number of predefined buckets, and MM is the number of unique values that have been inserted into the HashSet.
'''

