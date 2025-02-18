Given an array A of length N, return the subarray from B to C.

Code:
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        subarray = []

        # Append elements from index B to C to the subarray
        for i in range(B, C + 1):
            subarray.append(A[i])

        return subarray
