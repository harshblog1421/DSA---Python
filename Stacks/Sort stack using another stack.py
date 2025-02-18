Given a stack of integers A, sort it using another stack.
Return the array of integers after sorting the stack using another stack.

Problem Constraints
1 <= |A| <= 5000
0 <= A[i] <= 109

Input Format
The only argument is a stack given as an integer array A.

Output Format
Return the array of integers after sorting the stack using another stack.

Example Input
Input 1:
 A = [5, 4, 3, 2, 1]
Input 2:
 A = [5, 17, 100, 11]

Example Output
Output 1:
 [1, 2, 3, 4, 5]
Output 2:
 [5, 11, 17, 100]

Example Explanation
Explanation 1:
 Just sort the given numbers.
Explanation 2:
 Just sort the given numbers.



from collections import deque
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        st1 = deque()
        st2 = deque()
        for i in range(len(A)):
            while len(st1)>0 and st1[-1]>A[i]:
                x = st1.pop()
                st2.append(x)

            st1.append(A[i])

            if len(st2)>0:
                while len(st2)>0:
                    st1.append(st2.pop())

        result = []
        while len(st1):
            result.append(st1.pop())

        result.reverse()
        
        return result
                

