Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Problem Constraints
1 <= number of nodes <= 105
-100000 <= B, value of nodes <= 100000

Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B denoting the sum.

Output Format
Return 1, if there exist root-to-leaf path such that adding up all the values along the path equals the given sum. Else, return 0.

Example Input
Input 1:

 Tree:    5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1

 B = 22
Input 2:

 Tree:    5
         / \
        4   8
       /   / \
     -11 -13  4

 B = -1

Example Output
Output 1:
 1
  
Output 2:
 0


Example Explanation

Explanation 1:

 There exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which has sum 22. So, return 1.
Explanation 2:

 There is no path which has sum -1.





# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):
            curr =0
            def check(node,curr,B):

                if node is None:
                    return 0

                curr += node.val

                if curr == B and node.left is None and node.right is None:
                    return 1

                return check(node.left,curr,B) or check(node.right,curr,B)
            return check(A,curr,B)
                

    
