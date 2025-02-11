Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.
NOTE: All the A integers will fit in 32-bit integers.

Problem Constraints
1 <= A <= 29500

Input Format
The only argument given is integer A.

Output Format
Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.

Example Input
Input 1:
 A = 3
Input 2:
 A = 7

Example Output
Output 1:
 [1, 2, 3]
Output 2:
 [1, 2, 3, 11, 12, 13, 21]

Example Explanation
Explanation 1:
 Output denotes the first 3 integers that contains only digits 1, 2 and 3.

Explanation 2:
 Output denotes the first 7 integers that contains only digits 1, 2 and 3.




from collections import deque

class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        result = []
        queue = deque(['1', '2', '3'])  # Initialize the queue with '1', '2', '3'
        
        while len(result) < A:
            # Get the front element from the queue
            current = queue.popleft()
            
            # Append the current number to the result list
            result.append(int(current))
            
            # Generate the next numbers and add them to the queue
            for digit in ['1', '2', '3']:
                queue.append(current + digit)
        
        return result

