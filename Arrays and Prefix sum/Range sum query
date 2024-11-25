You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of long
    def rangeSum(self, A, B):
        n = len(A)
        psum = [0] * n  # Prefix sum array
        psum[0] = A[0]
        
        # Build the prefix sum array
        for i in range(1, n):
            psum[i] = psum[i - 1] + A[i]

        result_array = []
        # Process each query
        for i in range(len(B)):
            l = B[i][0]  # Start index of range
            r = B[i][1]  # End index of range
            
            # Calculate range sum using prefix sum
            if l == 0:
                result = psum[r]
            else:
                result = psum[r] - psum[l - 1]
            
            result_array.append(result)

        return result_array
