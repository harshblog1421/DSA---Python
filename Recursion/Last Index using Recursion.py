You are given an array A of size N. Write a recursive function that returns the last index at which an integer B is found in the array.

NOTE: If B is not found anywhere in the array then return -1.


def search(A,B,i,index):
    
    if i<0:
        return -1

    if A[i] ==B:
        index =i
        return index

    return search(A,B,i-1,index)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def LastIndex(self, A, B):
        index = -1
        return search(A,B,len(A)-1,index)


