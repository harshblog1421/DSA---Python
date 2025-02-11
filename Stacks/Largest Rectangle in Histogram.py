Given an array of integers A.
A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.
Find the area of the largest rectangle formed by the histogram.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10000

Input Format
The only argument given is the integer array A.

Output Format
Return the area of the largest rectangle in the histogram.

Example Input
Input 1:
 A = [2, 1, 5, 6, 2, 3]
Input 2:
 A = [2]

Example Output
Output 1:
 10
Output 2:
 2

Example Explanation
Explanation 1:
The largest rectangle has area = 10 unit. Formed by A[3] to A[4].

Explanation 2:
Largest rectangle has area 2.


from collections import deque 
def prev_smaller(arr):

    st = deque()
    result = [-1] *len(arr)
    for i in range(len(arr)):
        while len(st) and arr[st[-1]] >= arr[i]:
            st.pop()

        if len(st)>0:
            result[i] = st[-1]

        st.append(i)
    
    return result

def next_smaller(arr):
    
    st = deque()
    result = [-1]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        while len(st) and arr[st[-1]] >= arr[i]:

            st.pop()

        if len(st)>0:
            result[i] = st[-1]

        st.append(i)

    return result



class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
        result = -100000000000
        nxt = next_smaller(A)
        prev = prev_smaller(A)
        for i in range(len(A)):
            if nxt[i] ==-1:
                nxt[i] = len(A)
            result = max(result,A[i] *(nxt[i] - prev[i] -1))

        return result
