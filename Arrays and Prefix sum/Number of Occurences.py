Given an array A and an integer B, find the number of occurrences of B in A.

Code:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for i in range(len(A)):
            if A[i]==B:
                count +=1

        return count
