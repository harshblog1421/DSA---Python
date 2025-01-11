Given an integer A.
Two numbers, X and Y, are defined as follows:

X is the greatest number smaller than A such that the XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A, such that the XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.

NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.

NOTE 2: Your code will be run against a maximum of 100000 Test Cases.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #x + y = (x ^ y) + 2 * (x & y)
        #from above formula we need have x&y as zero result wen need to get x^y, for this x bit should be oppsoite of y bits 
        # x = 101 , value of y should be 010
        n=A
        #please assign a to n bcoz A should remain for later part of the code
        count=0

        #count number of bit positions for given A
        while n>0:
            count+=1
            n = n>>1

        #get the new valuex=0  by setting 0's poisiont of A to 1's
        x=0
        for i in range(count):
            if ( A & (1 << i) ) == 0:
                x = x | (1 << i)

       #y will be very next 2**i value,so do leftshift on 1 ro get that value of (10 or 100 or 1000 or 1000 ...... and so on)         
        y = 1<<count

        #Now x is a value which is just greatest number smaller than A 
        #y is value which is 
        #return the final output
        return x ^ y
