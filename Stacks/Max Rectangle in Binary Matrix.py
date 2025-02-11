Given a 2-D binary matrix A of size N x M filled with 0's and 1's, find the largest rectangle containing only ones and return its area.
Problem Constraints
1 <= N, M <= 100

Input Format
The first argument is a 2-D binary array A.

Output Format
Return an integer denoting the area of the largest rectangle containing only ones.

Example Input
Input 1:
 A = [
       [1, 1, 1]
       [0, 1, 1]
       [1, 0, 0] 
     ]

Input 2:
 A = [
       [0, 1, 0]
       [1, 1, 1]
     ] 

Example Output
Output 1:
 4
Output 2:
 3

Example Explanation
Explanation 1:
 As the max area rectangle is created by the 2x2 rectangle created by (0, 1), (0, 2), (1, 1) and (1, 2).
Explanation 2:
 As the max area rectangle is created by the 1x3 rectangle created by (1, 0), (1, 1) and (1, 2).





from collections import deque

def prev_smaller(A):

    result= [-1]*len(A)
    st = deque()
    for i in range(len(A)):
        
        while len(st) and A[st[-1]] >= A[i]:
            st.pop()

        if len(st)>0:
            result[i] = st[-1]

        st.append(i)

    return result

def prev_greater(A):

    result = [-1]*len(A)
    st = deque()

    for i in range(len(A)):
        while len(st) and A[st[-1]]<= A[i]:
            st.pop()

        if len(st)>0:
            result[i] = st[-1]

        st.append(i)

    return result


def next_greater(A):
    result = [-1]*len(A)

    st = deque()

    for i in range(len(A)-1,-1,-1):
        while len(st) and A[st[-1]] <= A[i]:
            st.pop()

        if len(st)>0:
            result[i] = st[-1]

        st.append(i)

    return result

def next_smaller(A):

    result = [-1]*(len(A))
    st = deque()

    for i in range(len(A)-1,-1,-1):
        while len(st) and A[st[-1]] >= A[i]:
            st.pop()

        if len(st)>0:
            result[i] = st[-1]

        st.append(i)

    return result
    
def max_histogram(A):

    nxt = next_smaller(A)
    prev = prev_smaller(A)
    n = len(A)
    curr = 0

    for i in range(len(A)):

        if nxt[i] ==-1:
            nxt[i] = len(A)

        curr = max(curr,A[i]*(nxt[i] - prev[i] -1))

    return curr
        
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
        
        curr_row = A[0]
        ans = max_histogram(A[0])

        for i in range(1,len(A)):
            for j in range(len(A[0])):

                if A[i][j] ==0:
                    curr_row[j] = 0

                else:
                    curr_row[j] +=1

            curr_ans = max_histogram(curr_row)

            ans = max(curr_ans, ans)

        return ans

            

