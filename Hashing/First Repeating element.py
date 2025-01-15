Given an integer array A of size N, find the first repeating element in it.
We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
If there is no repeating element, return -1.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
The first and only argument is an integer array A of size N.

Output Format
Return an integer denoting the first repeating element.

Example Input
Input 1:
 A = [10, 5, 3, 4, 3, 5, 6]

Input 2:
 A = [6, 10, 5, 4, 9, 120]

Example Output
Output 1:
 5

Output 2:
 -1

Example Explanation
Explanation 1:
 5 is the first element that repeats

Explanation 2:
 There is no repeating element, output -1

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Initialize a hashmap to store the frequency of each element
        hm = {}
        
        # Count the occurrences of each element in the array
        for i in range(len(A)):
            if A[i] in hm:
                hm[A[i]] += 1
            else:
                hm[A[i]] = 1

        # Find and return the first element with a frequency greater than 1
        for i in hm:
            if hm[i] > 1:
                return i
        
        # Return -1 if no duplicate element is found
        return -1
