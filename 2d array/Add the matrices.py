You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.

Code:

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        # Get the number of rows in matrix A
        N = len(A)
        # Get the number of columns in matrix A
        M = len(A[0])
        # Initialize the result matrix C with zeros, of size N x M
        C = [[0]*M for _ in range(N)]

        # Iterate over each row of the matrix
        for i in range(len(A)):
            # Iterate over each column of the current row
            for j in range(len(A[i])):
                # Add the corresponding elements of A and B and store in C
                C[i][j] = A[i][j] + B[i][j]
        
        # Return the resulting matrix C
        return C
