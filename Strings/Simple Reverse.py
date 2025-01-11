Given a string A, you are asked to reverse the string and return the reversed string.

class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        # Convert the string to a list of characters
        B = list(A)
        N = len(B)
        i = 0
        j = N - 1
        
        # Swap characters from both ends to reverse the string
        while i < j:
            B[i], B[j] = B[j], B[i]
            i += 1
            j -= 1
        
        # Return the reversed string
        return ''.join(B)

        
