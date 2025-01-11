Given two positive integers A and B. Implement Fast Power function to compute AB

Note : Please use the approach taught in the class.

210 = 25 * 25 
25 = 32, so 32 * 32 = 1024

def fast_pow(x,n):

    if n==0:
        return 1
    if x ==0:
        return 0
    half = fast_pow(x,n//2)
    if n%2==0:
        return half*half
    else:
        return half*half*x
    
class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def power(self, A, B):
        x = fast_pow(A,B)
        return x
