Given a Binary Search Tree(BST) A. If there is a node with value B present in the tree delete it and return the tree.
Note - If there are multiple options, always replace a node by its in-order predecessor

Problem Constraints
2 <= No. of nodes in BST <= 105
1 <= value of nodes <= 109
Each node has a unique value

Input Format
The first argument is the root node of a Binary Search Tree A.
The second argument is the value B.

Output Format
Delete the given node if found and return the root of the BST.

Example Input
Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 10

Input 2:

            8
           / \
          6  21
         / \
        1   7

     B = 6



Example Output
Output 1:

            15
          /    \
        12      20
        / \    /  \
       8  14  16  27

Output 2:

            8
           / \
          1  21
           \
            7



Example Explanation

Explanation 1:

Node with value 10 is deleted 
Explanation 2:

Node with value 6 is deleted 



# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def delete_node(root,target):

    if root is None:
        return None
    
    if root.val == target:
        
        if root.left ==None and root.right == None:
            return None

        if root.left == None:
            return root.right

        if root.right ==None:
            return root.left

        temp = root.left
        while temp is not None:
            temp = temp.right
        root.val = temp.val

        root.left = delete_node(root.left, temp.val)

    elif root.val < target:
        return delete_node(root.right, target)

    elif root.val >target:
        return delete_node(root.left, target)

    return root

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def solve(self, A, B):

        x = delete_node(A,B)
        return x
