Given a Binary Search Tree A. Check whether there exists a node with value B in the BST.

Problem Constraints
1 <= Number of nodes in binary tree <= 105
0 <= B <= 106

Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B.

Output Format
Return 1 if such a node exist and 0 otherwise

Example Input
Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 16

Input 2:

            8
           / \
          6  21
         / \
        1   7

     B = 9


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 Node with value 16 is present.
Explanation 2:

 There is no node with value 9.




# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def search(node,target):

    if node is None:
        return 0

    if node.val == target:
        return 1

    if node.val < target:
        return search(node.right,target)

    if node.val > target:
        search(node.left,target)


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

            
