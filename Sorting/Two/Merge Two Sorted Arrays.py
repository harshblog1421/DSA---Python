Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.
Note: A linear time complexity is expected and you should avoid use of any library function.

Problem Constraints
-2×109 <= A[i], B[i] <= 2×109
1 <= |A|, |B| <= 5×104


Input Format
First Argument is a 1-D array representing  A.
Second Argument is also a 1-D array representing B.

Output Format
Return a 1-D vector which you got after merging A and B.

Example Input
Input 1:
A = [4, 7, 9]
B = [2, 11, 19]

Input 2:
A = [1]
B = [2]

Example Output
Output 1:
[2, 4, 7, 9, 11, 19]

Output 2:
[1, 2]


Example Explanation
Explanation 1:
Merging A and B produces the output as described above.

Explanation 2:
 Merging A and B produces the output as described above.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        # Length of the first tuple
        n = len(A)
        # Length of the second tuple
        m = len(B)
        
        # Pointers for traversing A and B
        i = 0
        j = 0
        
        # Resultant list to store the merged output
        res = []

        # Merge elements from both tuples A and B in sorted order
        while i < n and j < m:
            if A[i] <= B[j]:  # If current element of A is smaller or equal to the current element of B
                res.append(A[i])  # Append A[i] to the result
                i += 1  # Move pointer in A
            else:
                res.append(B[j])  # Append B[j] to the result
                j += 1  # Move pointer in B

        # If there are remaining elements in A, add them to the result
        while i < n:
            res.append(A[i])
            i += 1

        # If there are remaining elements in B, add them to the result
        while j < m:
            res.append(B[j])
            j += 1

        # Return the merged sorted list
        return res
