You are given a string S, and you have to find all the amazing substrings of S.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input
Only argument given is string S.

Output
Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Initialize the count of amazing substrings
        count = 0
        # Define the set of vowels
        vowels = set("aeiouAEIOU")
        
        # Loop through each character in the string
        for i in range(len(A)):
            # If the character is a vowel, count the substrings starting from here
            if A[i] in vowels:
                count += len(A) - i
        
        # Return the count modulo 10003
        return count % 10003
