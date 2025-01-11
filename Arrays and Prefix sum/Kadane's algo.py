class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # Initialize variables to keep track of the current sum and maximum sum
        curr_sum = 0
        max_sum = -10000000  # Start with a very small number
        
        # Iterate through the array
        for i in range(len(A)):
            # Calculate the current sum by adding A[i] and resetting if negative
            curr_sum = A[i] + max(curr_sum, 0)
            # Update the maximum sum if the current sum is greater
            max_sum = max(curr_sum, max_sum)

        # Return the maximum sum found
        return max_sum

