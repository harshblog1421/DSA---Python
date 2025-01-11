You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array

Note : The order of the subarrays in the resulting 2D array does not matter.

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        list_subarrays = []

        # Generate all subarrays by fixing the start and end indices
        for si in range(len(A)):
            for ei in range(si, len(A)):
                subarray = []
                for m in range(si, ei + 1):
                    subarray.append(A[m])
                list_subarrays.append(subarray)

        return list_subarrays
