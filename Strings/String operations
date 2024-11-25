Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:

Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.

NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        # Concatenate the string with itself
        B = A + A
        
        # Initialize an empty list to store the resultant string
        C = []
        
        # Iterate through the string B
        for i in range(len(B)):
            # Skip uppercase letters
            if 65 <= ord(B[i]) <= 90:
                pass
            # Replace vowels with '#'
            elif B[i] in ("a", 'e', 'i', 'o', 'u'):
                C.append("#")
            # Append lowercase letters to the result
            elif 97 <= ord(B[i]) <= 122:
                C.append(B[i])
        
        # Return the transformed string
        return ''.join(C)
