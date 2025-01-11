Given an array A of size N, write a recursive function that returns the maximum element of the array.

def find_max(A,index):
    if index >= len(A):
        return float('-inf')
    
    mx = max(A[index],find_max(A,index+1))

    return mx
class Solution:
    # @param A : list of integers
    # @return an integer
    def getMax(self, A):
        x = find_max(A,0)
        return x
