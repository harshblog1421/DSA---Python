Given a number A. Return 1 if A is prime and return 0 if not. 

Note : 
The value of A can cross the range of Integer.

class Solution:
    def solve(self, A):
        count = 0
        # Iterate through potential divisors up to the square root of A
        for i in range(1, int(A**0.5) + 1):
            if A % i == 0:
                # If divisors are the same, count it once (perfect square case)
                if i == A // i:
                    count += 1
                else:
                    # Otherwise, count both divisors
                    count += 2

        # A prime number has exactly 2 divisors (1 and itself)
        if count == 2:
            return 1
        else:
            return 0

