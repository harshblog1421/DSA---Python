Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        maj = -1
        count = 0

        # First pass to find potential majority element
        for i in range(len(A)):
            if count == 0:
                maj = A[i]
                count = 1
            elif maj == A[i]:
                count += 1
            else:
                count -= 1

        # Second pass to verify if the majority element actually occurs more than n/2 times
        c = 0
        for i in range(len(A)):
            if A[i] == maj:
                c += 1
        if c > n // 2:
            return maj
        return -1  # No majority element
