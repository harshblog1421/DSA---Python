You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note: If you end up using an additional array, you will only receive partial score.

Code:
class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        # Get the number of columns (m) and rows (n) in the matrix
        m = len(A[0])
        n = len(A)
        # Initialize the transposed matrix with size m x n
        transposed = [[0] * n for i in range(m)]
        
        # Transpose the matrix
        for i in range(len(A)):
            for j in range(len(A[i])):
                # Assign the element to its transposed position
                transposed[j][i] = A[i][j]

        # Reverse each row in the original matrix
        for i in range(len(transposed)):
            for j in range(len(transposed[i]) // 2):
                # Swap elements to reverse the row
                A[i][j], A[i][n - 1 - j] = A[i][n - 1 - j], A[i][j]

        # Return the transposed matrix
        return transposed


