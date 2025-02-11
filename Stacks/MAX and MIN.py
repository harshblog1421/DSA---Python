Given an array of integers A.
The value of an array is computed as the difference between the maximum element in the array and the minimum element in the array A.
Calculate and return the sum of values of all possible subarrays of A modulo 109+7.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 1000000

Input Format
The first and only argument given is the integer array A.

Output Format
Return the sum of values of all possible subarrays of A modulo 109+7.

Example Input
Input 1:
 A = [1]

Input 2:
 A = [4, 7, 3, 8]

Example Output
Output 1:
 0
Output 2:
 26

Example Explanation
Explanation 1:
Only 1 subarray exists. Its value is 0.
Explanation 2:
value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26




from collections import deque

def previoussmaller(arr,n):
    
    st = deque()
    ans = [-1]*n
    for i in range(len(arr)):
        while len(st)>0 and arr[st[-1]]>= arr[i]:
            st.pop()
        
        if len(st)>0:
            ans[i] = st[-1]

        st.append(i)

    return ans

def previousgreater(arr,n):
    
    st = deque()
    ans = [-1]*n
    for i in range(len(arr)):
        while len(st)>0 and arr[st[-1]]<= arr[i]:
            st.pop()
        
        if len(st)>0:
            ans[i] = st[-1]

        st.append(i)

    return ans

def nextgreater(arr,n):
    
    st = deque()
    ans = [-1]*n
    for i in range(len(arr)-1,-1,-1):
        while len(st)>0 and arr[st[-1]]<= arr[i]:
            st.pop()
        
        if len(st)>0:
            ans[i] = st[-1]

        st.append(i)

    return ans

def nextsmaller(arr,n):
    
    st = deque()
    ans = [-1]*n
    for i in range(len(arr)-1,-1,-1):
        while len(st)>0 and arr[st[-1]]>= arr[i]:
            st.pop()
        
        if len(st)>0:
            ans[i] = st[-1]

        st.append(i)

    return ans


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ps = previoussmaller(A,n)
        ns = nextsmaller(A,n)
        pg = previousgreater(A,n)
        ng = nextgreater(A,n)

        ans = 0
        for i in range(len(A)):

            if ns[i]==-1:
                ns[i] = len(A)

            if ng[i] ==-1:
                ng[i] = len(A)

            ans += A[i] * (((i-pg[i])*(ng[i]-i)) - ((i-ps[i])*(ns[i]-i)))

        x = ans%(10**9 + 7)
        return x
