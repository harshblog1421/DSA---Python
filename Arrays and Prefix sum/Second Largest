You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        B = set(A)  # Remove duplicates
        Max = -10**18  # Initialize maximum
        Max_2 = -10**18  # Initialize second maximum

        # If there are less than 2 unique elements, return -1
        if len(B) < 2:
            return -1

        else:
            for i in range(len(A)):
                # Update max and second max
                if A[i] > Max:
                    Max_2 = Max
                    Max = A[i]
                elif Max_2 < A[i] < Max:
                    Max_2 = A[i]

        return Max_2

