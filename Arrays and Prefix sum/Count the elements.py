Given an array A of N integers. 
Count the number of elements that have at least 1 elements greater than itself.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Find the maximum value in the list
        Max = max(A)
        # Initialize a counter for numbers less than the maximum
        count = 0
        # Iterate through the list
        for i in range(len(A)):
            if A[i] < Max:
                count += 1
        # Return the count of numbers less than the maximum
        return count

            
