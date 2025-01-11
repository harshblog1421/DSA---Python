Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Note: A palindrome is a string that's the same when read forward and backward.

Problem Constraints
1 <= |A| <= 50000

String A consists only of lowercase letters.

Input Format
The first and only argument is a string A.

Output Format
Return 1 if the string A is a palindrome, else return 0.

Example Input

Input 1:
 A = "naman"

Input 2:
 A = "strings"

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 "naman" is a palindomic string, so return 1.

Explanation 2:
 "strings" is not a palindrome, so return 0.

def pallindrome(A,start,end):
    if A[start]!=A[end]:
        return False

    if start>=end:
        return True

    return pallindrome(A,start+1,end-1)
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        x = pallindrome(A,0,len(A)-1)
        if x is True:
            return 1
        else:
            return 0
