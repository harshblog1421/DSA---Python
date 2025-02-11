Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with the sum of elements greater than B.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the maximum value of K (sub array length).

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 10

Input 2:
A = [5, 17, 100, 11]
B = 130

Example Output
Output 1:
 2

Output 2:
 3

Example Explanation
Explanation 1:
For K = 5, There are subarrays [1, 2, 3, 4, 5] which has a sum > B
For K = 4, There are subarrays [1, 2, 3, 4], [2, 3, 4, 5] which has a sum > B
For K = 3, There is a subarray [3, 4, 5] which has a sum > B
For K = 2, There were no subarray which has a sum > B.
Constraints are satisfied for maximal value of 2.

Explanation 2:
For K = 4, There are subarrays [5, 17, 100, 11] which has a sum > B
For K = 3, There were no subarray which has a sum > B.
Constraints are satisfied for maximal value of 3.


def is_value(A,B,K):

    curr_sum = 0

    i = 0
    j = K-1

    while i<=j:
        curr_sum+=A[i]
        i+=1

    if curr_sum >B:
        return False

    i = 1
    j = K

    while j<len(A):
        curr_sum = curr_sum + A[j] - A[i-1]

        if curr_sum > B:
            return False

        i+=1
        j+=1

    return True

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start = 1
        end = len(A)
        ans = 0

        while start<=end:

            mid = (start+end)//2

            if is_value(A,B,mid):
                ans = mid
                start = mid+1

            else:
                end = mid - 1

        return ans
