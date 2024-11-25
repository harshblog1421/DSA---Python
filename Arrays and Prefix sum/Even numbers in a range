You are given an array A of length N and Q queries given by the 2D array B of size Q×2.
Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]]

Code:
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        # Initialize prefix sum array for even numbers
        psum = [0] * len(A)
        # Set the prefix sum for the first element
        if A[0] % 2 == 0:
            psum[0] = 1
        else:
            psum[0] = 0

        # Build prefix sum array
        for i in range(1, len(A)):
            if A[i] % 2 == 0:
                psum[i] = psum[i - 1] + 1
            else:
                psum[i] = psum[i - 1]

        # Initialize the result array
        result_array = []

        # Process each query in B
        for j in range(len(B)):
            l = B[j][0]
            r = B[j][1]
            result = 0

            # Calculate the count of even numbers in the range
            if l == 0:
                result = psum[r]
            else:
                result = psum[r] - psum[l - 1]

            # Append the result to the result array
            result_array.append(result)

        # Return the result array
        return result_array
