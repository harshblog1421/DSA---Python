Given the inorder and postorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the inorder traversal of the tree.
Second argument is an integer array B denoting the postorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input
Input 1:

 A = [2, 1, 3]
 B = [2, 3, 1]

Input 2:

 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]


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
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def in_to_post(inorder,postorder,instart,inend,poststart,postend):

    if instart > inend or poststart>postend:
        return None

    root_val = postorder[postend]
    root = TreeNode(root_val)

    position = -1
    for i in range(instart,inend+1):
        if inorder[i] == root_val:
            position = i
            break

    leftsize = position-instart
    rightsize = inend- position

    root.left = in_to_post(inorder,postorder,instart,position-1,poststart,poststart+leftsize-1)
    root.right = in_to_post(inorder,postorder,position+1,inend,poststart +leftsize, postend-1)

    return root
    

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):

        n = len(A)
        return in_to_post(A,B,0,n-1,0,n-1)
