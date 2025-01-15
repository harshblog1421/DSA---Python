Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).

Problem Constraints
1 <= length of the array <= 105
1 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the number of inversions of A modulo (109 + 7).

Example Input
Input 1:
A = [1, 3, 2]

Input 2:
A = [3, 4, 1, 2]

Example Output

Output 1:
1

Output 2:
4

Example Explanation
Explanation 1:
The pair (1, 2) is an inversion as 1 < 2 and A[1] > A[2]

Explanation 2:
The pair (0, 2) is an inversion as 0 < 2 and A[0] > A[2]
The pair (0, 3) is an inversion as 0 < 3 and A[0] > A[3]
The pair (1, 2) is an inversion as 1 < 2 and A[1] > A[2]
The pair (1, 3) is an inversion as 1 < 3 and A[1] > A[3]

def merge_sort(arr,l,r):
    counter = 0
    if l<r:
        mid = (l+r)//2
        
        counter+=merge_sort(arr,l,mid)
        counter+=merge_sort(arr,mid+1,r)
        counter+=merge(arr,l,mid,r)
    
    return counter

def merge(A,l,mid,r):
    i = l
    j = mid + 1
    k = 0
    B = [0] * (r - l + 1)
    counter = 0
    
    while i <= mid and j <= r:
        if A[i] <= A[j]:  # <= instead of <
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            counter += (mid - i + 1)  # Adjusted the inversion count calculation
            j += 1
        k += 1
    
    if j>mid:
        while i <= mid:
            B[k] = A[i]
            i += 1
            k += 1
    
    if i>mid:
        while j <= r:
            B[k] = A[j]
            j += 1
            k += 1

    for k in range(r - l + 1):
        A[l + k] = B[k]

    return counter

    
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        X = merge_sort(A,0,n-1)
        return X%(10**9+7)
            

        
        
