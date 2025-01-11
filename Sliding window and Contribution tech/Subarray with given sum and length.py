Given an array A of length N. Also given are integers B and C.

Return 1 if there exists a subarray with length B having sum C and 0 otherwise

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        sub_sum = 0
        # Calculate sum for the first subarray of length B
        for i in range(B):
            sub_sum += A[i]
            if sub_sum == C:
                return 1  # Return 1 if sum equals C for first subarray

        # Use sliding window technique for subsequent subarrays of length B
        i = 1
        j = B
        while j < len(A):
            sub_sum = sub_sum + A[j] - A[i-1]  # Slide the window
            if sub_sum == C:
                return 1  # Return 1 if sum equals C for any subarray
            i += 1
            j += 1
        
        return 0  # Return 0 if no subarray with sum C is found
