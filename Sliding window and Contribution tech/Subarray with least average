Given an array A of size N, find the subarray of size B with the least average.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        index = 0
        sum1 = 0

        # Calculate the sum for the first subarray of size B
        for i in range(B):
            sum1 += A[i]

        ans = sum1  # Initialize answer with the sum of the first subarray

        # Use sliding window technique for subsequent subarrays
        i = 1
        j = B
        while j < len(A):
            sum1 = sum1 + A[j] - A[i-1]  # Slide the window
            if sum1 < ans:  # Update answer if new subarray has a smaller sum
                ans = sum1
                index = i  # Store the starting index of the subarray
            i += 1
            j += 1

        return index  # Return the index of the subarray with the least average
