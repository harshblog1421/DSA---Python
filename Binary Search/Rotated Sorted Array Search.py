Given a sorted array of integers A of size N and an integer B, 
where array A is rotated at some pivot unknown beforehand.
For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].
Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.
You can assume that no duplicates exist in the array.
NOTE: You are expected to solve this problem with a time complexity of O(log(N)).

Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 109
All elements in A are Distinct.

Input Format
The First argument given is the integer array A.
The Second argument given is the integer B.

Output Format
Return index of B in array A, otherwise return -1

Example Input
Input 1:
A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4 

Input 2:
A : [ 9, 10, 3, 5, 6, 8 ]
B : 5

Example Output
Output 1:
 0 

Output 2:
 3

Example Explanation
Explanation 1:
Target 4 is found at index 0 in A. 

Explanation 2:
Target 5 is found at index 3 in A.

def binary(A,start,end):

    l = start
    r = end
    n = len(A)
    ans = n

    while l<=r:
        mid = (l+r)//2

        if A[mid]>=A[0]:
            # we are on the left side, go right
            l = mid+1

        elif A[mid]<A[0]:
            ans = mid
            r = mid-1

        else:
            return ans
    return ans

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):

        n = len(A)
        pivot = binary(A,0,n-1)

        if B>=A[0]:
            l = 0
            r = pivot-1

        else:
            l = pivot
            r = n-1

        
        while l<=r:
            mid = (l+r)//2

            if B<A[mid]:
                r = mid-1

            elif B>A[mid]:
                l = mid+1

            else:
                return mid

        return -1
