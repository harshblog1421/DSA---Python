Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()  # Sort the array to make sure we check the progression correctly
        diff = A[1] - A[0]  # Calculate the difference between the first two elements
        
        # Loop through the rest of the array
        for i in range(2, len(A)):
            # If the difference between consecutive elements is not the same, return 0
            if diff != A[i] - A[i - 1]:
                return 0

        return 1  # Return 1 if the array is in arithmetic progression

