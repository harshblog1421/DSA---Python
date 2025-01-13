Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.
Find the maximum value of GCD.

Problem Constraints
2 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the maximum value of GCD.

Example Input
Input 1:
 A = [12, 15, 18]

Input 2:
 A = [5, 15, 30]

Example Output
Output 1:
 6

Output 2:
 15

Example Explanation
Explanation 1:
 If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum value of gcd is 6.

Explanation 2:
 If you delete 5, gcd will be 15.
 If you delete 15, gcd will be 5.
 If you delete 30, gcd will be 5.
 Maximum value of gcd is 15.


def gcd(A,B):
    if B==0:
        return A
    return gcd(B,A%B)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A):

        n = len(A)

        if n<=0:
            return A[0]

        prefix_gcd = [0]*n
        suffix_gcd = [0]*n

        prefix_gcd[0] = A[0]
        for i in range(1,len(A)):
            prefix_gcd[i] = gcd(prefix_gcd[i-1],A[i])

        suffix_gcd[n-1] = A[n-1]
        for i in range(n-2,-1,-1):
            suffix_gcd[i] = gcd(suffix_gcd[i+1],A[i])

        max_gcd = 0
        for i in range(n):
            if i==0:
                current_gcd = suffix_gcd[i+1]

            elif i==n-1:
                current_gcd = prefix_gcd[i-1]

            else:
                current_gcd = gcd(prefix_gcd[i-1],suffix_gcd[i+1])

            max_gcd = max(max_gcd,current_gcd)

        return max_gcd
