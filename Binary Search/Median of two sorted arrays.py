Given two sorted arrays A and B of size M and N respectively, return the median of the two sorted arrays.
Round of the value to the floor integer [2.6=2, 2.2=2]

Problem Constraints
0 <= M <= 105
0 <= N <= 105
-109 <= A[i], B[i] <= 109

Input Format
First argument A is an array of integers.
First argument B is an array of integers.

Output Format
Return an integer.

Example Input
Input 1:
A = [1, 3]
B = [2]

Input 2:
A = [1, 2]
B = [3,4]

Example Output
Output 1:
3

Output 2:
3

Example Explanation
Example 1:
merged array = [1,2,3] and median is 2.
Example 2:
merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2



class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        
        if len(B)<len(A):
            return self.solve(B,A)

        n1 = len(A)
        n2 = len(B)
        N = n1+n2
        start = 0
        end = n1

        while start<=end:
            mid = (start+end)//2
            cut1 = mid
            cut2 = N//2 - cut1

            l1 = float('-inf') if cut1 == 0 else A[cut1-1]
            l2 = float('-inf') if cut2 == 0 else B[cut2-1]
            r1 = float('inf') if cut1 == n1 else A[cut1]
            r2 = float('inf') if cut2 == n2 else B[cut2]

            if l1<=r2 and l2<=r1:

                if N%2 ==0:
                    return ((max(l1,l2) + min(r1,r2))//2)

                else:
                    return min(r1,r2)

            elif l1>r2:
                end = cut1 -1

            else:
                start = cut1+1

        return 0

