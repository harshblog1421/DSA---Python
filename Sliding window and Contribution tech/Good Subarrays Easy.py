Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Initialize a prefix sum array
        psum = [0]*len(A)
        psum[0] = A[0]
        
        # Calculate prefix sum for the array
        for i in range(1, len(A)):
            psum[i] = psum[i-1] + A[i]

        count = 0
        # Iterate through all possible subarrays
        for l in range(len(A)):
            for r in range(l, len(A)):
                sub_sum = 0
                # Calculate subarray sum using prefix sum
                if l == 0:
                    sub_sum = psum[r]
                else:
                    sub_sum = psum[r] - psum[l-1]
                
                # Check the conditions for good subarray (length and sum conditions)
                if sub_sum < B and (r - l + 1) % 2 == 0 or sub_sum > B and (r - l + 1) % 2 != 0:
                    count += 1
            
        return count

