Given a root of binary tree A, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Problem Constraints
1 <= size of tree <= 100000

Input Format
First and only argument is the root of the tree A.


Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Example Input
Input 1:

    1
   / \
  2   3

Input 2: 
       1
      /
     2
    /
   3


Example Output

Output 1:

1

Output 2:

0


Example Explanation

Explanation 1:

It is a complete binary tree.
Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1. 





# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def check_balance(A):

    if A is None:
        return 0

    left_height = check_balance(A.left)
    right_height = check_balance(A.right)

    if left_height == -1 or right_height ==-1:
        return -1

    if abs(left_height - right_height )>1:
        return -1

    return 1+max(left_height,right_height)

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):

        x = check_balance(A)
        if x ==-1:
            return 0

        else:
            return 1
