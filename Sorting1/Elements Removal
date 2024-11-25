Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        cost = 0  # Variable to track the total cost
        A.sort(reverse=True)  # Sort the array in descending order
        
        # Calculate the cost for removing each element
        for i in range(N):
            cost += A[i] * (i + 1)  # The cost is the element times its position
        
        return cost  # Return the total cost

