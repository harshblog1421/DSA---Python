You are given an array A of integers of length N and two indices, B and C.
Your task is to sort the subarray [B, C] within the given array. The rest of the array should remain unchanged.

Problem Constraints
1 ≤ N ≤ 105
0 ≤ A[i] ≤ 109
0 ≤ B ≤ C ≤ N - 1

Input Format
First argument is the array A of length N. The next two arguments are the integers B and C.

Output Format
Return the array after sorting the [B, C] subarray.

Example Input
Input:
A = [59, 11, 8, 91, 49, 44, 8]
B = 4
C = 6

Input 2:
A = [50, 40, 30, 20, 10]
B = 0
C = 3

Example Output
Output:
[59, 11, 8, 91, 8, 44, 49]

Output:
[20, 30, 40, 50, 10]

Example Explanation
Explanation 1:

Initially the subarray [B, C], i.e. A[4, 6] = [49, 44, 8].
After sorting this becomes [8, 44, 49].
It can be seen that this subarray gets sorted and rest of the array remains unchanged!

Explanation 2:
Initially the subarray [B, C], i.e. A[0, 3] = [50, 40, 30, 20].
After sorting this becomes [20, 30, 40, 50].
It can be seen that this subarray gets sorted and rest of the array remains unchanged!

# Function to partition the array
def partition(A, first, last):
    # Choose the first element as the pivot
    pivot = A[first]
    left = first + 1  # Pointer starting just after the pivot
    right = last      # Pointer starting at the end of the array

    # Loop to rearrange elements around the pivot
    while left <= right:
        # If the left element is smaller than or equal to the pivot, move the pointer to the right
        if A[left] <= pivot:
            left += 1
        # If the right element is greater than the pivot, move the pointer to the left
        elif A[right] > pivot:
            right -= 1
        # If the left element is greater and the right element is smaller, swap them
        else:
            A[left], A[right] = A[right], A[left]

    # Place the pivot in its correct position by swapping it with the element at right
    A[first], A[left - 1] = A[left - 1], A[first]

    # Return the final position of the pivot
    return left - 1

# Recursive Quick Sort function
def quick_sort(arr, start, end):
    # Base case: if the start index is greater than the end index, return
    if start > end:
        return

    # Partition the array and get the pivot index
    pivot_index = partition(arr, start, end)

    # Recursively sort the left and right subarrays
    quick_sort(arr, start, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)

# Solution class with the method to sort a subarray
class Solution:
    # @param A : list of integers
    # @param B : integer (start index of subarray)
    # @param C : integer (end index of subarray)
    # @return a list of integers
    def sortSubarray(self, A, B, C):
        # Apply quick sort only on the subarray from index B to C
        quick_sort(A, B, C)
        # Return the updated array
        return A
