You have given a string A having Uppercase English letters.

You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.

Code:

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        total = 0
        count = 0

        # Loop through the string and count occurrences of 'A' and 'G'
        for i in range(len(A)):
            if A[i] == "A":
                count += 1  # Increase count when 'A' is found
            elif A[i] == "G":
                total += count  # Add the number of 'A's before 'G'

        return total

