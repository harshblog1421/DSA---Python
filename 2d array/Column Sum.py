You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.

Code:
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        # Initialize a list to store the sum of each column
        Sum_column = []
        
        # Iterate through each column index
        for i in range(len(A[0])):
            # Initialize the sum for the current column
            sum1 = 0
            # Iterate through each row index
            for j in range(len(A)):
                # Add the value of the current cell to the column sum
                sum1 += A[j][i]
            # Append the column sum to the result list
            Sum_column.append(sum1)
        
        # Return the list of column sums
        return Sum_column

