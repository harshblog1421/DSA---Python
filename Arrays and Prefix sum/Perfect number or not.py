You are given an integer A. You have to tell whether it is a perfect number or not.

Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

A proper divisor of a natural number is the divisor that is strictly less than the number.


Code:

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Initialize a variable to store the sum of divisors
        sum = 0
        # Iterate through numbers from 1 to A-1
        for i in range(1, A):
            if A % i == 0:  # Check if i is a divisor of A
                sum += i  # Add the divisor to the sum
        # A number is perfect if the sum of its divisors equals the number itself
        if sum == A:
            return 1  # Return 1 if the number is perfect
        else:
            return 0  # Otherwise, return 0

