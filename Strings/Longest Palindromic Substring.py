Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index)

class Solution:
    # @param A : string
    # @return a string
    def longestPalindrome(self, A):
        # Initialize variables to track the longest palindrome
        ans = 0
        start = -1
        end = -1
        
        # Loop through each character in the string (odd length palindromes)
        for i in range(len(A)):
            l = i
            r = i
            
            # Expand around the center as long as the characters match
            while l >= 0 and r < len(A):
                if A[l] != A[r]:
                    break
                l -= 1
                r += 1
                # Update the palindrome if it's longer than the current one
                if r - l - 1 > ans:
                    start = l + 1
                    end = r - 1
                    ans = max(ans, r - l - 1)
        
        # Loop through each character again (even length palindromes)
        for j in range(len(A)-1):
            l = j
            r = j + 1
            
            # Expand around the center as long as the characters match
            while l >= 0 and r < len(A):
                if A[l] != A[r]:
                    break
                l -= 1
                r += 1
                # Update the palindrome if it's longer than the current one
                if r - l - 1 > ans:
                    start = l + 1
                    end = r - 1
                    ans = max(ans, r - l - 1)
        
        # Return the longest palindrome substring
        return A[start:end+1]
