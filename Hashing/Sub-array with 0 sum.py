Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1, else return 0.

Problem Constraints
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9

Input Format
The only argument given is the integer array A.

Output Format
Return whether the given array contains a subarray with a sum equal to 0.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]

Input 2:
 A = [4, -1, 1]

Example Output
Output 1:
0

Output 2:
1

# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hs = set()
        ongoing = 0
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        for i in range(len(A)):
            ongoing+=A[i]

            if ongoing ==0:
                return 1

            if ongoing in hs:
                return 1
            
            hs.add(ongoing)

        return 0

            
