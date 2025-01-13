Given an array of integers A, calculate the sum of A [ i ] % A [ j ] for all possible i, j pairs. Return sum % (109 + 7) as an output.

Problem Constraints
1 <= length of the array A <= 105
1 <= A[i] <= 103

Input Format
The only argument given is the integer array A.

Output Format
Return a single integer denoting sum % (109 + 7).

Example Input
Input 1:
 A = [1, 2, 3]
Input 2:
 A = [17, 100, 11]

Example Output
Output 1:
 5
Output 2:
 61


Example Explanation
Explanation 1:
 (1 % 1) + (1 % 2) + (1 % 3) + (2 % 1) + (2 % 2) + (2 % 3) + (3 % 1) + (3 % 2) + (3 % 3) = 5

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        frq = [0]*1001

        for i in range(len(A)):
            frq[A[i]] +=1


        total_sum = 0
        for y in range(1,1001):
                if frq[y] ==0:
                    continue
                curr_sum = 0
                for x in range(1,1001):
                        if frq[x] ==0:
                            continue
                        remainder = y%x
                        curr_sum = (curr_sum + remainder*frq[x]) % (10**9+7)

                total_sum = (total_sum + curr_sum * frq[y]) % (10**9+7)

        return total_sum
