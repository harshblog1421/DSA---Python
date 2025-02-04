You are given an integer array A of size N.

You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.

Find and return the maximum possible sum of the B elements that were removed after the B operations.

NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.

Code:class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0

        n = len(A)
        # Create prefix sum array for the first B elements
        psum = [0] * n
        psum[0] = A[0]
        for i in range(1, n):
            psum[i] = psum[i - 1] + A[i]

        # Create suffix sum array for the last B elements
        ssum = [0] * n
        ssum[-1] = A[-1]
        for i in range(n - 2, -1, -1):
            ssum[i] = ssum[i + 1] + A[i]

        # Max sum possible from removing B elements from one end of the array
        ans = max(psum[B - 1], ssum[n - B])

        # Try combinations of removing from both ends
        sum1 = 0
        for k in range(1, B):
            sum1 = psum[k - 1] + ssum[n - B + k]
            ans = max(sum1, ans)

        return ans
