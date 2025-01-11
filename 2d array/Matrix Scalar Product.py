You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.

Code:
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        for i in range(len(A)):
#iterate for rows
            for j in range(len(A[i])):
            #iterate for columns
                A[i][j] = B*A[i][j]
               # multiply each element of matrix with B
        return A
