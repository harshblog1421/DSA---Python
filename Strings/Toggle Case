You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.

You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.

class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        # Convert the string into a list of characters
        word = [x for x in A]
        
        # Iterate through each character and toggle its case
        for i in range(len(word)):
            # If the character is uppercase, convert it to lowercase
            if 65 <= ord(word[i]) <= 90:
                word[i] = chr(ord(word[i]) + 32)
            # If the character is lowercase, convert it to uppercase
            else:
                word[i] = chr(ord(word[i]) - 32)
        
        # Return the string with toggled cases
        return ''.join(word)
