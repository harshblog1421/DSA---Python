Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        # Return the original array if indices are invalid
        if B < 0 or B > C or C >= len(A):
            return A

        # Reverse elements between indices B and C
        while B < C:
            A[B], A[C] = A[C], A[B]
            B += 1
            C -= 1

        return A

