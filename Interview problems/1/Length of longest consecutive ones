Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # To count all 1's in the string
        count_one = 0
        n = len(A)

        # Count the number of 1's in the string
        for i in range(len(A)):
            if A[i] == '1':
                count_one += 1

        # Arrays to store the consecutive 1's from left and right
        left = [0] * n
        right = [0] * n

        # Initialize left and right for boundary cases
        if A[0] == '1':
            left[0] = 1
        if A[n - 1] == '1':
            right[n - 1] = 1

        # Fill left array with consecutive 1's count from the left
        for j in range(1, len(A) - 1):
            if A[j] == '1':
                left[j] = left[j - 1] + 1

        # Fill right array with consecutive 1's count from the right
        for j in range(n - 2, -1, -1):
            if A[j] == '1':
                right[j] = right[j + 1] + 1

        max_count = 0
        # Find the maximum consecutive 1's without swap
        for i in range(n):
            max_count = max(max_count, max(left[i], right[i]))

        # Try swapping each '0' with '1' to see if it creates a longer sequence
        for i in range(1, n - 1):
            if A[i] == '0':
                count = left[i - 1] + right[i + 1]
                if count < count_one:
                    count += 1
                max_count = max(max_count, count)

        return max_count
