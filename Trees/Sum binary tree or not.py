Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.
Sum-binary Tree is a Binary Tree where the value of a every node is equal to sum of the nodes present in its left subtree and right subtree.
An empty tree is Sum-binary Tree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.
Return 1 if it sum-binary tree else return 0.

Problem Constraints
1 <= length of the array <= 100000
0 <= node values <= 50

Input Format
The only argument given is the root node of tree A.

Output Format
Return 1 if it is sum-binary tree else return 0.

Example Input
Input 1:

       26
     /    \
    10     3
   /  \     \
  4   6      3


Input 2:
       26
     /    \
    10     3
   /  \     \
  4   6      4


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 All leaf nodes are considered as SumTree. 
 Value of Node 10 = 4 + 6.
 Value of Node 3 = 0 + 3 
 Value of Node 26 = (10 + 4 + 6) + 6 

Explanation 2:

 Sum of left subtree and right subtree is 27 which is not equal to the value of root node which is 26.





# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def check_node(node):

    if node is None:
        return 0

    left_sum = check_node(node.left)
    right_sum = check_node(node.right)

    if left_sum ==-1 or right_sum ==-1:
        return -1

    if node.right or node.left:
        if left_sum + right_sum !=node.val:
            return -1

    subtree_sum = left_sum + right_sum + node.val

    return subtree_sum
    
    

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

            X = check_node(A)
            if X ==-1:
                return 0 
            else:
                return 1

        
