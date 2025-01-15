Given an array A of N integers.
Find the length of the longest subarray in the array which sums to zero.
If there is no subarray which sums to zero then return 0.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
Single argument which is an integer array A.

Output Format
Return an integer.

Example Input
Input 1:
 A = [1, -2, 1, 2]

Input 2:
 A = [3, 2, -1]

Example Output
Output 1:
3

Output 2:
0

Example Explanation
Explanation 1:
 [1, -2, 1] is the largest subarray which sums up to 0.

Explanation 2:
 No subarray sums up to 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hm = {}
        ans = 0
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            
            # If cumulative sum is zero, update answer to include this subarray
            if sum == 0:
                ans = max(ans, i + 1)
            
            # If sum is seen before, update the answer with the distance
            if sum in hm:
                ans = max(ans, i - hm[sum])
            else:
                # Store the first occurrence of this cumulative sum
                hm[sum] = i
        
        return ans
