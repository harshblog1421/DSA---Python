Write a function that takes an integer and returns the number of 1 bits present in its binary representation.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        
        count = 0
        while A>0:
            if A&1>0:
                count+=1
            A = A>>1
        return count
