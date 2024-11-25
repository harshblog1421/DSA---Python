Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Create a prefix sum array to store the cumulative sum of elements
        psum = [0] * len(A)
        psum[0] = A[0]
        
        # Calculate the prefix sum for the array A
        for i in range(1, len(A)):
            psum[i] = psum[i-1] + A[i]
        
        count = 0  # Initialize count to store the number of subarrays with sum less than B
        
        # Loop through all possible subarrays using two pointers, l and r
        for l in range(len(A)):
            for r in range(l, len(A)):
                sub_sum = 0  # Variable to store the sum of the current subarray
                
                # Calculate the sum of the subarray A[l...r] using the prefix sum array
                if l == 0:
                    sub_sum = psum[r]
                else:
                    sub_sum = psum[r] - psum[l-1]
                
                # Check if the subarray sum is less than B
                if sub_sum < B:
                    count += 1  # Increment count if condition is satisfied
        
        return count  # Return the total count of good subarrays
