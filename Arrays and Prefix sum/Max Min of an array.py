Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        Max = max(A)
        Min = min(A)
        return Max+Min
        
