Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).
Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Problem Constraints
1 <= length of array <= 100000

Input Format
First argument is an integer array A.

Output Format
Return a root node of the Binary Search Tree.


Example Input
Input 1:
 A : [1, 2, 3]
Input 2:
 A : [1, 2, 3, 5, 10]


Example Output
Output 1:
      2
    /   \
   1     3
Output 2:
      3
    /   \
   2     5
  /       \
 1         10


Example Explanation

Explanation 1:

 You need to return the root node of the Binary Tree.




# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct(A,start,end):
    
        if start>end:
            return
    
        mid = (start+end)//2

        root = TreeNode(A[mid])
        root.left = construct(A,start,mid-1)
        root.right = construct(A,mid+1,end)

        return root

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
            n = len(A)
            return construct(A,0,n-1)
             
