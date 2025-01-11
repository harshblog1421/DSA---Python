Given two binary strings A and B. Return their sum (also a binary string).

class Solution:
    # @param A : string
    # @param B : string
    # @return a string
    def addBinary(self, A, B):
        result = []  # To store the result
        i, j = len(A) - 1, len(B) - 1  # Start from the last bit of both binary numbers
        carry = 0  # Initialize carry to 0

        # Loop until both strings are processed and there's no carry left
        while i >= 0 or j >= 0 or carry:
            # Get the current bit of A and B (if available)
            bit_a = int(A[i]) if i >= 0 else 0
            bit_b = int(B[j]) if j >= 0 else 0
        
            total = bit_a + bit_b + carry  # Add the two bits and the carry
            carry = total // 2  # Update carry (1 if total >= 2, else 0)
            result.append(str(total % 2))  # Store the current bit (either 0 or 1)
        
            i -= 1  # Move to the previous bit of A
            j -= 1  # Move to the previous bit of B
    
        return ''.join(result[::-1])  # Reverse the result and join to form the binary sum
