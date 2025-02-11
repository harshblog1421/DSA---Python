You are given a binary tree represented by root A. You need to check if it is a Binary Search Tree or not.

Assume a BST is defined as follows:
1) The left subtree of a node contains only nodes with keys less than the node's key.
2) The right subtree of a node contains only nodes with keys greater than the node's key.
3) Both the left and right subtrees must also be binary search trees.


Problem Constraints
1 <= Number of nodes in binary tree <= 105
0 <= node values <= 232-1


Input Format
First and only argument is head of the binary tree A.

Output Format
Return 0 if false and 1 if true.

Example Input
Input 1:
   1
  /  \
 2    3

Input 2:

  2
 / \
1   3


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 2 is not less than 1 but is in left subtree of 1.
Explanation 2:

Satisfies all conditions.




# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
        def helper(root,array):
            if root is None:
                return 
            helper(root.left,array)
            array.append(root.val)
            helper(root.right,array)
        
        result = []
        helper(A,result)

        for i in range(1,len(result)):
            if result[i-1]>result[i]:
                return 0 
            
        return 1

