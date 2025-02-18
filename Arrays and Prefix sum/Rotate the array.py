Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times towards the right.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        # Rotate the array B times
        for i in range(B):
            temp = A[n - 1]  # Store the last element
            # Shift all elements one position to the right
            for j in range(n - 2, -1, -1):
                A[j + 1] = A[j]
            A[0] = temp  # Place the last element at the front
        return A
