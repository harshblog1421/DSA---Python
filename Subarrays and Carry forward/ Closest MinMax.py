Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Find the maximum and minimum values in the array
        Max = max(A)
        Min = min(A)
        # Initialize variables for tracking the last occurrence of max and min values
        last_max = -1
        last_min = -1
        ans = 10**15  # Set a very high initial answer value

        # If Max and Min are the same, the smallest subarray is of size 1
        if Max == Min:
            return 1

        # Loop through the array to find the smallest subarray
        for i in range(len(A)):
            # If current element is the max value, update last_max
            if A[i] == Max:
                last_max = i
                # If the minimum value has been found before, calculate the length of the subarray
                if last_min != -1:
                    ans = min(ans, i - last_min + 1)

            # If current element is the min value, update last_min
            elif A[i] == Min:
                last_min = i
                # If the maximum value has been found before, calculate the length of the subarray
                if last_max != -1:
                    ans = min(ans, i - last_max + 1)

        # Return the length of the smallest subarray found
        return ans
