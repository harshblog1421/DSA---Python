Given an integer A, you need to find the count of it's factors.

Factor of a number is the number which divides it perfectly leaving no remainder.

Example : 1, 2, 3, 6 are factors of 6

Cclass Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Initialize variables
        i = 1
        count = 0
        # Iterate to find divisors
        while i * i <= A:
            if A % i == 0:
                count += 1
                # Check if the divisor pair is unique
                if i != A // i:
                    count += 1
            i += 1
        # Return the count of divisors
        return count

      
