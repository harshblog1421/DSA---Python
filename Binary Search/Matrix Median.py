Given a matrix of integers A of size N x M in which each row is sorted.
Find and return the overall median of matrix A.
NOTE: No extra memory is allowed.
NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
1 <= N, M <= 10^5
1 <= N*M <= 10^6
1 <= A[i] <= 10^9
N*M is odd

Input Format
The first and only argument given is the integer matrix A.

Output Format
Return the overall median of matrix A.

Example Input
Input 1:
A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ] 

Input 2:
A = [   [5, 17, 100]    ]

Example Output
Output 1:
 5 

Output 2:
 17

Example Explanation
Explanation 1:
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5. 
Explanation 2:
Median is 17.


def findsmaller_element(A, assumed_median):
    no_of_smaller_elements = 0

    for row in A:
        start, end = 0, len(row) - 1

        while start <= end:
            mid = (start + end) // 2

            if row[mid] <= assumed_median:
                start = mid + 1
            else:
                end = mid - 1

        # After binary search, 'start' will point to the count of elements <= assumed_median
        no_of_smaller_elements += start

    return no_of_smaller_elements


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        N = len(A)
        M = len(A[0])
        total_elements = N * M
        median_index = total_elements // 2

        # Define the range of binary search
        start = min(row[0] for row in A)
        end = max(row[-1] for row in A)

        while start <= end:
            assumed_median = (start + end) // 2
            lesser_elements = findsmaller_element(A, assumed_median)

            if lesser_elements <= median_index:
                start = assumed_median + 1
            else:
                end = assumed_median - 1

        # Directly return 'start' as the median
        return start

