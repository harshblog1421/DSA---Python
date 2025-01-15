Given an integer array A of length N, considering the last element as pivot p, rearrange the elements such that for all i:
if A[i] < p then it should be present on left side of the partition
if A[i] > p then it should be present on right side of the partition
Rearrange the given array as well as return the partition index.

Note: All elements are distinct

Problem Constraints
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 109

Input Format
The only input argument is the given vector A.

Output Format
Return the partition index as well as rearrange the input array to satisfy the given conditions.

Example Input
Input:
A = [6, 2, 0, 4, 5]

Example Output
Output:
 Valid
A possible solution can be:
A = [2, 0, 4, 5, 6] and partitionIndex = 3

Example Explanation
Explanation:
 The rearrangement is valid because every element in [0, 2] index range is less than the pivot element, and every element in [3, 4] index range is greater than the pivot element.

# Function to perform partitioning using a pivot
def pivot(A, start, end):
    # Choose the last element as the pivot
    pivot = A[end]
    left = start      # Pointer starting from the first element
    right = end - 1   # Pointer starting just before the pivot

    # Loop until the pointers cross
    while left <= right:
        # If the left element is smaller or equal to the pivot, move the left pointer to the right
        if A[left] <= pivot:
            left += 1
        # If the right element is greater than the pivot, move the right pointer to the left
        elif A[right] > pivot:
            right -= 1
        # If the left element is greater and the right element is smaller, swap them
        else:
            A[left], A[right] = A[right], A[left]
    
    # Swap the pivot with the element at the left pointer
    A[end], A[left] = A[left], A[end]

    # Return the final position of the pivot
    return left

# Function to partition the array and return the pivot index
def partition(arr):
    n = len(arr)  # Get the length of the array
    return pivot(arr, 0, n - 1)  # Call pivot on the entire array
