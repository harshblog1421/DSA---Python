Given an integer array A of size N. In one second, you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        total = 0
        Max = max(A)  # Find the maximum element in the array
        for i in range(len(A)):
            # Calculate the difference needed to make A[i] equal to Max
            diff = Max - A[i]
            total += diff  # Add the difference to the total

        return total
