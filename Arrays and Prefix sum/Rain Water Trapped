class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        left_max = [0] * n  # Array to store max height to the left of each index
        right_max = [0] * n  # Array to store max height to the right of each index
        sum1 = 0  # Variable to accumulate trapped water

        # Fill left_max array
        left_max[0] = A[0]
        for i in range(1, len(A)):
            left_max[i] = max(A[i], left_max[i - 1])

        # Fill right_max array
        right_max[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], A[i])

        # Calculate trapped water
        for i in range(len(A)):
            sum1 += min(right_max[i], left_max[i]) - A[i]

        return sum1
