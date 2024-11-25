Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.


The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

class Solution:
    # @param A : list of strings
    # @return a string
    def longestCommonPrefix(self, A):
        # If the array is empty, return an empty string
        if not A:
            return ""
        
        # Start with the first string as the prefix
        prefix = A[0]
        
        # Iterate through all the strings in the list
        for i in range(len(A)):
            # While the current string does not start with the prefix
            while not A[i].startswith(prefix):
                # Shorten the prefix by one character
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""
        
        # Return the final common prefix
        return prefix
