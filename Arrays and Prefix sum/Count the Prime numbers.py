You will be given an integer n. You need to return the count of prime numbers less than or equal to n.

Code:

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Initialize a counter for prime numbers
        cnt = 0
        # Iterate through numbers from 1 to A
        for i in range(1, A + 1):
            factors = 0
            # Check divisors for the current number
            for j in range(1, i + 1):
                if i % j == 0:
                    factors += 1
            # Increment count if the number has exactly 2 factors (prime number)
            if factors == 2:
                cnt += 1
        # Return the count of prime numbers
        return cnt

