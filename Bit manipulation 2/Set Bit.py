You are given two integers A and B.
Set the A-th bit and B-th bit in 0, and return output in decimal Number System.

Note:
The bit positions are 0-indexed, which means that the least significant bit (LSB) has index 0.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
    
        return 0|(1<<A)|(1<<B)
           

        
