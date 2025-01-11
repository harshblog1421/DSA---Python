You are given a string A of size N.


Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string

class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        # Split the string into words
        X = A.split()
        
        # Reverse the list of words
        C = X[::-1]
        
        # Join the reversed words back into a single string
        return ' '.join(C)
