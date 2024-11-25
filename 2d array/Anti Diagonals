Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.

Code:
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        # Get the number of rows in the matrix
        n = len(A)
        # Get the number of columns in the matrix
        m = len(A[0])
        # Initialize the result matrix B with zeros, of size (2*n - 1) x n
        B = [[0]*n for _ in range(2*n - 1)]

        # Process the upper triangle of the matrix, including the main diagonal
        for c in range(len(A)):
            i = 0  # Row index starts at 0
            j = c  # Column index starts at c
            while i < n and j >= 0:
                # Place the element of A into the appropriate position in B
                B[i + j][n - 1 - j] = A[i][j]
                i += 1  # Move down the row
                j -= 1  # Move left in the column

        # Process the lower triangle of the matrix (below the main diagonal)
        for k in range(1, len(A)):
            i = k  # Row index starts at k
            j = m - 1  # Column index starts at the last column
            while i < n and j >= 0:
                # Place the element of A into the appropriate position in B
                B[i + j][n - 1 - j] = A[i][j]
                i += 1  # Move down the row
                j -= 1  # Move left in the column

        # Reverse each row in B for the final output
        for k in range(len(B)):
            B[k] = B[k][::-1]

        # Return the resulting matrix B
        return B
