You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        max_sum = 0  # Initialize max sum as 0

        # Iterate through the array to find subarrays
        for i in range(len(C)):
            sub_sum = 0
            # Sum each subarray and check if the sum exceeds B
            for j in range(i, len(C)):
                sub_sum += C[j]
                if sub_sum > B:  # Stop if sum exceeds B
                    break
                max_sum = max(max_sum, sub_sum)  # Update max sum if current subarray has higher sum

        return max_sum

