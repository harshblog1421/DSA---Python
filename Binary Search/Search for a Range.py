Given a sorted array of integers A (0-indexed) of size N, find the left most and the right most index of a given integer B in the array A.
Return an array of size 2, such that 
          First element = Left most index of B in A
          Second element = Right most index of B in A.
          If B is not found in A, return [-1, -1].

Note : Note: The time complexity of your algorithm must be O(log n)..

Problem Constraints
1 <= N <= 106
1 <= A[i], B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the left most and right most index (0-based) of B in A as a 2-element array. If B is not found in A, return [-1, -1].

Example Input
Input 1:
 A = [5, 7, 7, 8, 8, 10]
 B = 8

Input 2:
 A = [5, 17, 100, 111]
 B = 3

Example Output
Output 1:
 [3, 4]

Output 2:
 [-1, -1]


Example Explanation
Explanation 1:
 The first occurrence of 8 in A is at index 3.
 The last occurrence of 8 in A is at index 4.
 ans = [3, 4]

Explanation 2:
 There is no occurrence of 3 in the array.



class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        A = list(A)
        ans1 = -1
        ans2 = -1
        n = len(A)
        start1 = 0
        start2 = 0
        end1 = n-1
        end2 = n-1
        result = []

        # for the first occurence of the element
        while start1<=end1:

            mid1 = (start1+end1)//2

            if A[mid1]<B:
                start1 = mid1+1

            elif A[mid1]>B:
                end1 = mid1-1
            else:
                ans1 = mid1
                end1 = mid1-1

        while start2<=end2:
            mid2 = (start2+end2)//2

            if A[mid2]<B:
                start2 = mid2+1

            elif A[mid2]>B:
                end2 = mid2-1

            else:
                ans2 = mid2
                start2 = mid2+1

        result.append(ans1)
        result.append(ans2)

        return result
