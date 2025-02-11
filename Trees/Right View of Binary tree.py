Given a binary tree of integers denoted by root A. Return an array of integers representing the right view of the Binary tree.
Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.

Problem Constraints

1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9


Input Format
First and only argument is head of the binary tree A.


Output Format
Return an array, representing the right view of the binary tree.

Example Input
Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output

Output 1:

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]


Example Explanation

Explanation 1:

Right view is described.
Explanation 2:

Right view is described.



from collections import deque
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        q = deque()

        q.append(A)
        last = A
        array = []

        while len(q)>0:
            x = q.popleft()

            if x.left is not None:
                q.append(x.left)

            if x.right is not None:
                q.append(x.right)

            if x ==last:
                array.append(x.val)
                if len(q)>0:
                    last = q[-1]

        return array
