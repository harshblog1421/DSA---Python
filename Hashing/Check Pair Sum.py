Given an Array of integers B, and a target sum A.
Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.

Problem Constraints
1 <= Length of array B <= 105
0 <= Bi <= 109
0 <= A <= 109

Input Format
First argument A is the Target sum, and second argument is the array B

Output Format
Return an integer value 1 if there exists such pair, else return 0.

Example Input
Input 1:
A = 8   
B = [3, 5, 1, 2, 1, 2]

Input 2:
A = 21   
B = [9, 10, 7, 10, 9, 1, 5, 1, 5]

Example Output
Output 1:
1

Output 2:
0

Example Explanation
Example 1:
It is possible to obtain sum 8 using 3 and 5.

Example 2:
There is no such pair exists.

class Solution:
    # @param A : integer (target value)
    # @param B : list of integers (array)
    # @return an integer (1 if pair exists, 0 otherwise)
    def solve(self, A, B):
        # Swap A and B for clarity in processing
        A, B = B, A

        # Use a set to store elements of A for efficient lookups
        hm = set()

        # Traverse the array to find if the target pair exists
        for i in range(len(A)):
            # Check if the complement (B - A[i]) exists in the set
            if B - A[i] in hm:
                return 1  # Pair found

            # Add the current element to the set
            else:
                hm.add(A[i])

        # Return 0 if no such pair is found
        return 0
