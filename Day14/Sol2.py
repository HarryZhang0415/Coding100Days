# Approach 2: Mathematical Deduction

'''
Actually, as it turns out, the sequence of G(n)G(n) function results is known as Catalan number C_nC 
n
​	
 . And one of the more convenient forms for calculation is defined as follows:

C0 = 0; Cn+1 = 2(2n+1)/(n+2) * Cn

We skip the proof here, which one can find following the above reference.
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)