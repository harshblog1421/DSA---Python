Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.

class Solution:
    def solve(self, A, B):
        n = len(A)
        # Create a prefix sum array to store cumulative sums
        pref = [0] * n
        pref[0] = A[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + A[i]
        
        ans = 0

        # Check every subarray
        for i in range(n):
            for j in range(i, n):
                val = pref[j]
                if i > 0:
                    val -= pref[i-1]
                # If the subarray sum is less than B, increment the answer
                if val < B:
                    ans += 1
        return ans
