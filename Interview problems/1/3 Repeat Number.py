You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Note: Read-only array means that the input array should not be modified in the process of solving the problem

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
    
        # Handle edge cases where the array is empty or has only one element
        if n==0:
            return -1
        if n==1:
            return A[0]

        # Initialize two potential candidates
        first = A[0]
        second = A[1]
        count1 = 1
        count2 = 1

        # Traverse through the array to find the potential candidates
        for i in range(2, n):
            if A[i] == first:
                count1 += 1
            elif A[i] == second:
                count2 += 1
            elif count1 == 0:
                first = A[i]
                count1 = 1
            elif count2 == 0:
                second = A[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Count the occurrences of the candidates
        for i in range(len(A)):
            if A[i] == first:
                count1 += 1
            elif A[i] == second:
                count2 += 1

        # Return the candidate that occurs more than n//3 times
        if count1 > n // 3:
            return first
        elif count2 > n // 3:
            return second
        return -1

