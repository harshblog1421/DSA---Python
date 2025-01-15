You are given an array A of N elements. Sort the given array in increasing order of number of distinct factors of each element, i.e., element having the least number of factors should be the first to be displayed and the number having highest number of factors should be the last one. If 2 elements have same number of factors, then number with less value should come first.
Note: You cannot use any extra space

Problem Constraints
1 <= N <= 104
1 <= A[i] <= 104

Input Format
First argument A is an array of integers.

Output Format
Return an array of integers.

Example Input
Input 1:
A = [6, 8, 9]

Input 2:
A = [2, 4, 7]

Example Output
Output 1:
[9, 6, 8]

Output 2:
[2, 7, 4]


Example Explanation
For Input 1:
The number 9 has 3 factors, 6 has 4 factors and 8 has 4 factors.

For Input 2:
The number 2 has 2 factors, 7 has 2 factors and 4 has 3 factors.

import functools

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # Sort the list using a custom comparator defined by the `compare` function
        # `functools.cmp_to_key` converts the comparator function into a key function for sorting
        A = sorted(A, key=functools.cmp_to_key(self.compare))
        return A

    # Custom comparator function to compare two integers based on their factors
    def compare(self, v1, v2):
        # Calculate the number of factors for both numbers
        factors_v1 = self.factors(v1)
        factors_v2 = self.factors(v2)

        # If both numbers have the same number of factors, compare their values directly
        if factors_v1 == factors_v2:
            return v1 - v2  # Return the difference between the two numbers
        else:
            # Otherwise, compare based on the number of factors
            return factors_v1 - factors_v2

    # Helper function to calculate the number of factors of a number
    def factors(self, n):
        cnt = 0  # Initialize a counter for the number of factors
        i = 1    # Start with the smallest factor (1)
        
        # Iterate up to the square root of the number
        while i * i <= n:
            # If `i` is a factor of `n`
            if n % i == 0:
                # If `i` and `n/i` are the same (e.g., for perfect squares), count it once
                if i == n // i:
                    cnt += 1
                else:
                    # Otherwise, count both `i` and `n/i` as factors
                    cnt += 2
            i += 1  # Move to the next potential factor
        
        # Return the total count of factors
        return cnt
