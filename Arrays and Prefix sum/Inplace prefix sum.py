Given an array A of N integers. Construct prefix sum of the array in the given array itself.

Code:
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        for i in range(1,len(A)):
            A[i]=A[i]+A[i-1]  # just add the each previous element in currect element

        return A
