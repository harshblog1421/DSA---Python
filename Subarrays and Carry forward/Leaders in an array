Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.

NOTE: The rightmost element is always a leader.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_value = A[-1]  # Rightmost element is always a leader
        leaders = [A[-1]]
        
        # Traverse the array from the second-last element to the first
        for i in range(len(A) - 2, -1, -1):
            if A[i] > max_value:
                max_value = A[i]  # Update max_value if the current element is greater
                leaders.append(max_value)

        return leaders

        
