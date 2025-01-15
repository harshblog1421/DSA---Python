Given an integer array A, sort the array using Quick Sort.

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

# Function to partition the array
def partition(A, start, end):
    # Initialize pointers and choose the first element as the pivot
    l = start + 1  # Pointer for the left part of the array
    r = end        # Pointer for the right part of the array
    pivot = A[start]  # Choose the first element as the pivot

    # Loop to rearrange elements around the pivot
    while l <= r:
        # If the left pointer points to an element <= pivot, move it to the right
        if A[l] <= pivot:
            l += 1
        # If the right pointer points to an element > pivot, move it to the left
        elif A[r] > pivot:
            r -= 1
        # If the left element is greater than the pivot and the right element is smaller,
        # swap them to place them on the correct side of the pivot
        else:
            A[l], A[r] = A[r], A[l]

    # Place the pivot in its correct position
    A[start], A[l - 1] = A[l - 1], A[start]

    # Return the final position of the pivot
    return l - 1

# Recursive function to perform quick sort
def pivoting(A, start, end):
    # Base case: If the start index is greater than the end index, stop recursion
    if start > end:
        return

    # Partition the array and get the index of the pivot
    pivot_index = partition(A, start, end)

    # Recursively sort the elements to the left of the pivot
    pivoting(A, start, pivot_index - 1)

    # Recursively sort the elements to the right of the pivot
    pivoting(A, pivot_index + 1, end)

# Solution class to solve the problem
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self
