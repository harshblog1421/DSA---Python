Given an array A of both positive and negative integers.
Your task is to compute the sum of minimum and maximum elements of all sub-array of size B.
NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.

Problem Constraints
1 <= size of array A <= 105
-109 <= A[i] <= 109
1 <= B <= size of array

Input Format
The first argument denotes the integer array A.
The second argument denotes the value B

Output Format
Return an integer that denotes the required value.

Example Input
Input 1:
 A = [2, 5, -1, 7, -3, -1, -2]
 B = 4

Input 2:
 A = [2, -1, 3]
 B = 2

Example Output
Output 1:
 18

Output 2:
 3

Example Explanation
Explanation 1:
 Subarrays of size 4 are : 
    [2, 5, -1, 7],   min + max = -1 + 7 = 6
    [5, -1, 7, -3],  min + max = -3 + 7 = 4      
    [-1, 7, -3, -1], min + max = -3 + 7 = 4
    [7, -3, -1, -2], min + max = -3 + 7 = 4   
    Sum of all min & max = 6 + 4 + 4 + 4 = 18 

Explanation 2:
 Subarrays of size 2 are : 
    [2, -1],   min + max = -1 + 2 = 1
    [-1, 3],   min + max = -1 + 3 = 2
    Sum of all min & max = 1 + 2 = 3 


from collections import deque

def max_sliding(A,B):

    dq = deque()
    result = []
    # for maximum case
    for i in range(B):

        while len(dq)>0 and A[dq[-1]]<A[i]:
            dq.pop()
        dq.append(i)

    result.append(A[dq[0]])

    for i in range(B,len(A)):
        while len(dq)>0 and A[dq[-1]] < A[i]:
            dq.pop()

        dq.append(i)

        if dq[0] <= i-B:
            dq.popleft()

        result.append(A[dq[0]])

    return result

def min_sliding(A,B):

    dq = deque()
    result = []
    for i in range(B):
        while len(dq) >0 and A[dq[-1]]> A[i]:
            dq.pop()

        dq.append(i)

    result.append(A[dq[0]])

    for i in range(B,len(A)):
        while len(dq)>0 and A[dq[-1]] > A[i]:
            dq.pop()

        dq.append(i)

        if dq[0] <= i-B:
            dq.popleft()

        result.append(A[dq[0]])

    return result

        
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arr1 = max_sliding(A,B)
        arr2 = min_sliding(A,B)
        x = sum(arr1)
        y = sum(arr2)
        return (x+y)%(10**9 + 7)
            

