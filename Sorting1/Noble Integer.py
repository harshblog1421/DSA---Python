Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)  # Sort the array in descending order
        count = 0  # Initialize the counter
        if A[0] == 0:  # If the largest element is 0, return 1 (special case)
            return 1
        else:
            for i in range(1, len(A)):
                # Update the count whenever the element changes
                if A[i] != A[i - 1]:
                    count = i

                # If the count equals the element, return 1
                if count == A[i]:
                    return 1

        return -1  # Return -1 if no such element is found


        
