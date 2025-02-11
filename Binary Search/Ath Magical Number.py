You are given three positive integers, A, B, and C.
Any positive integer is magical if divisible by either B or C.
Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.
Note: Ensure to prevent integer overflow while calculating.

Problem Constraints
1 <= A <= 109
2 <= B, C <= 40000

Input Format
The first argument given is an integer A.
The second argument given is an integer B.
The third argument given is an integer C.

Output Format
Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

Example Input
Input 1:
 A = 1
 B = 2
 C = 3

Input 2:
 A = 4
 B = 2
 C = 3

Example Output
Output 1:
 2
Output 2:
 6

Example Explanation
Explanation 1:
 1st magical number is 2.
Explanation 2:
 First four magical numbers are 2, 3, 4, 6 so the 4th magical number is 6.


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)



class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        mod = 10**9 + 7
        low, high = 1, 2 * 10**14
        LCM_BC = lcm(B, C)
    
        while low < high:
            mid = (low + high) // 2
        # Calculate the count of magical numbers up to mid
            count = mid // B + mid // C - mid // LCM_BC
            if count < A:
                low = mid + 1
            else:
                high = mid
    
        return low % mod
