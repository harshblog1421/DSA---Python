Given an integer array A, sort the array using Merge Sort.

Problem Constraints
1 <= |A| <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return the sorted array.

Example Input
Input 1:-
A = [1, 4, 10, 2, 1, 5]

Input 2:-
A = [3, 7, 1]

Example Output
Output 1:-
[1, 1, 2, 4, 5, 10]

Output 2:-
[1, 3, 7]

Example Explanation
Explanation 1 and 2:
Return the sorted array.

# Function to perform merge sort
def merge_sort(A, l, r):
    # Base case: if the array has one or no elements, return (already sorted)
    if l >= r:
        return

    # Find the middle index to divide the array into two halves
    mid = (l + r) // 2

    # Recursively sort the left half
    merge_sort(A, l, mid)

    # Recursively sort the right half
    merge_sort(A, mid + 1, r)

    # Merge the two sorted halves
    merge_arr(A, l, r, mid)

# Helper function to merge two sorted halves of the array
def merge_arr(A, l, r, mid):
    # i points to the start of the left half, j points to the start of the right half
    i = l
    j = mid + 1

    # k is the index for the temporary array B
    k = 0

    # Temporary array to hold merged sorted elements
    B = [0] * (r - l + 1)

    # Merge elements from both halves into B
    while i <= mid and j <= r:
        if A[i] < A[j]:  # If element in left half is smaller
            B[k] = A[i]
            i += 1
        else:  # If element in right half is smaller
            B[k] = A[j]
            j += 1
        k += 1

    # If there are remaining elements in the right half, add them to B
    if i > mid:
        while j <= r:
            B[k] = A[j]
            j += 1
            k += 1
    else:
        # If there are remaining elements in the left half, add them to B
        while i <= mid:
            B[k] = A[i]
            i += 1
            k += 1

    # Copy the merged sorted elements from B back to the original array A
    for k in range(r - l + 1):
        A[l + k] = B[k]

    # Return the updated array (optional, since changes are made in-place)
    return A

# Solution class to apply merge sort on a given list
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)  # Get the size of the array
        merge_sort(A, 0, n - 1)  # Sort the array using merge_sort
        return A  # Return the sorted array
