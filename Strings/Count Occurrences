Find the number of occurrences of bob in string A consisting of lowercase English alphabets.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Initialize the count of occurrences of 'bob'
        count = 0
        
        # Loop through the string, checking substrings of length 3
        for i in range(len(A)-2):
            # If the current substring is 'bob', increment the count
            if A[i:i+3] == 'bob':
                count += 1
        
        # Return the total count
        return count
