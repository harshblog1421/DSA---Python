Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Initialize a set to store the elements we have seen
        seen = set()
        
        # Iterate through the array
        for i in range(len(A)):
            # Calculate the difference needed to form the sum B
            diff = B - A[i]
            # Check if the difference is already in the set
            if diff in seen:
                return 1  # Return 1 if such a pair exists
            else:    
                # Add the current element to the set
                seen.add(A[i])
        
        # If no such pair is found, return 0
        return 0

        
    
