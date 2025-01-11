You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0

        # Traverse through each element in the array
        for i in range(n):
            left_count = 0
            right_count = 0

            # Count elements smaller than A[i] to the left of A[i]
            for j in range(i):
                if A[j] < A[i]:
                    left_count += 1

            # Count elements greater than A[i] to the right of A[i]
            for j in range(i + 1, n):
                if A[i] < A[j]:
                    right_count += 1

            # Multiply left_count and right_count to get number of valid triplets
            ans += (left_count * right_count)

        return ans
