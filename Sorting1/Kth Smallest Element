Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)  # Convert the tuple to a list
        for i in range(0, B):
            min_idx = i  # Assume the first element is the minimum
            for j in range(i + 1, len(A)):
                # Find the index of the minimum element in the unsorted portion
                if A[min_idx] > A[j]:
                    min_idx = j
            # Swap the found minimum element with the element at the current index
            A[i], A[min_idx] = A[min_idx], A[i]
        
        return A[B - 1]  # Return the Bth smallest element
