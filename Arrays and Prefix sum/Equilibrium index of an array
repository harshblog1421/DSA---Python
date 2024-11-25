You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Calculate the total sum of the array
        total_sum = sum(A)
        # Initialize left and right sums
        left_sum = 0
        right_sum = 0

        # Iterate through the array to find the equilibrium index
        for i in range(len(A)):
            # Calculate right sum for the current index
            right_sum = total_sum - left_sum - A[i]
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i
            # Update left sum by adding the current element
            left_sum += A[i]

        # Return -1 if no equilibrium index is found
        return -1



