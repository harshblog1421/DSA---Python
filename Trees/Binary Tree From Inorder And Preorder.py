Given preorder and inorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the preorder traversal of the tree.
Second argument is an integer array B denoting the inorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input
Input 1:
 A = [1, 2, 3]
 B = [2, 1, 3]

Input 2:
 A = [1, 6, 2, 3]
 B = [6, 1, 3, 2]

Example Output
Output 1:
   1
  / \
 2   3
Output 2:

   1  
  / \
 6   2
    /
   3


Example Explanation

Explanation 1:

 Create the binary tree and return the root node of the tree.


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def buildtree_rec(inorder,preorder, instart, inend, prestart, pre_end):
    if instart > inend or prestart > pre_end:  # Base case
        return None

    # Create the root node
    root_val = preorder[prestart]
    root = TreeNode(root_val)

    # Find the root's index in the inorder list
    pos_root = -1
    for i in range(instart, inend + 1):
        if inorder[i] == root_val:
            pos_root = i
            break

    # Calculate sizes of left and right subtrees
    leftsize = pos_root - instart
    rightsize = inend - pos_root

    # Recursively build left and right subtrees
    root.left = buildtree_rec(inorder, preorder, instart, pos_root - 1, prestart+1, prestart + leftsize)
    root.right = buildtree_rec(inorder, preorder, pos_root + 1, inend, prestart + leftsize+1, pre_end)

    return root

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):

        n = len(A)
        return buildtree_rec(B, A, 0, n - 1, 0, n - 1)

        


