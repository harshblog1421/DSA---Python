You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.

Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).

Code:
class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        # Get the size of the square matrix (number of rows or columns)
        N = len(A)
        # Initialize row index (i) to 0 and column index (j) to N-1
        i = 0
        j = N - 1
        # Initialize a variable to store the sum of the anti-diagonal elements
        sum1 = 0
        
        # Traverse the matrix along its anti-diagonal
        while i < N and j >= 0:
            # Add the current anti-diagonal element to the sum
            sum1 += A[i][j]
            # Move to the next row
            i += 1
            # Move to the previous column
            j -= 1
        
        # Return the computed sum of the anti-diagonal elements
        return sum1



