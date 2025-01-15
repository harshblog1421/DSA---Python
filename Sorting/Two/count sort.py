Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.

Problem Constraints
1 <= |A| <= 105
1 <= A[i] <= 105

Input Format
The first argument is an integer array A.

Output Format
Return an integer array that is the sorted array A.

Example Input
Input 1:
A = [1, 3, 1]

Input 2:
A = [4, 2, 1, 3]

Example Output
Output 1:
[1, 1, 3]

Output 2:
[1, 2, 3, 4]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # Step 1: Find the length of the array
        n = len(A)
        
        # Step 2: Identify the minimum and maximum elements in the array
        mn = min(A)  # Minimum element in the array
        mx = max(A)  # Maximum element in the array
        
        # Step 3: Create a frequency array to count occurrences of each element
        # The size of the frequency array is determined by the range (mx - mn + 1)
        freq = [0] * (mx - mn + 1)

        # Step 4: Populate the frequency array
        # For each element in the input array, increment the corresponding index in the frequency array
        for i in range(len(A)):
            freq[A[i] - mn] += 1

        # Step 5: Build the sorted array
        arr = []  # Resultant sorted array
        for i in range(len(freq)):  # Iterate through the frequency array
            for k in range(freq[i]):  # Add the element `freq[i]` times to the result
                arr.append(i + mn)  # Reconstruct the original element using (i + mn)
        
        # Step 6: Return the sorted array
        return arr

Example Explanation

For Input 1:
The array in sorted order is [1, 1, 3].
For Input 2:
The array in sorted order is [1, 2, 3, 4].
