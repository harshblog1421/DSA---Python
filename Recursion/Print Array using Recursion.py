You are given an array A. Print the elements of the array using recursion.

NOTE :
You are required to not use any loops, You can create new functions.
Don't change the signature of the function PrintArray.
Print a new empty line after printing the output.


def print_array(A,index):
    if index >= len(A):
        return
    print(A[index],end = ' ')
    print_array(A,index+1)
    
class Solution:
    # @param A : list of integers
    def PrintArray(self, A):
        print_array(A,0)
        print()
