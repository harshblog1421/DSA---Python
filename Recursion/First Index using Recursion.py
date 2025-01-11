You are given an array A of size N. Write a recursive function that returns the first index at which an integer B is found in the array.

NOTE: If B is not found anywhere in the array then return -1.


def find(A,B,i):

    if i>=len(A):
        return -1

    if A[i]==B:
        return i
    
    return find(A,B,i+1)
    

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def FirstIndex(self, A, B):
        return find(A,B,0)

