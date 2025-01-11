Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Code:

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        # Get the number of rows (m) and columns (n) in the matrix
        m = len(A)
        n = len(A[0])
        # Initialize the transposed matrix with size n x m
        transposed = [[0] * m for _ in range(n)]
        # Iterate over each element in the matrix
        for i in range(m):
            for j in range(n):
                # Assign the element to its transposed position
                transposed[j][i] = A[i][j]
        # Return the transposed matrix
        return transposed

