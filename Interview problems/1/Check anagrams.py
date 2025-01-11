You are given two lowercase strings A and B each of length N. Return 1 if they are anagrams to each other and 0 if not.

Note : Two strings A and B are called anagrams to each other if A can be formed after rearranging the letters of B.


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        dict_A = {}
        dict_B = {}

        # Count frequency of characters in string A
        for i in A:
            if i in dict_A:
                dict_A[i] += 1
            else:
                dict_A[i] = 1

        # Count frequency of characters in string B
        for j in B:
            if j in dict_B:
                dict_B[j] += 1
            else:
                dict_B[j] = 1

        # Compare the frequency dictionaries of both strings
        if dict_A == dict_B:
            return 1  # Strings are anagrams
        else:
            return 0  # Strings are not anagrams
