You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.
More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
A subarray sum denotes the sum of all the elements of that subarray.

Note : Be careful of integer overflow issues while calculations. Use appropriate datatypes

class Solution:
    # @param A : list of integers
    # @return an long
    def subarraySum(self, A):
        ans = 0  # Initialize the answer variable

        # Traverse each element in the array
        for i in range(0, len(A)):
            # Calculate the contribution of each element to the subarray sum
            contribution = A[i] * (i + 1) * (len(A) - i)
            ans += contribution  # Add the contribution to the total sum
        
        return ans  # Return the total sum of all subarray sums
