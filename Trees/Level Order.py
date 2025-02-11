Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.


Output Format
Return a 2D integer array denoting the level order traversal of the given binary tree.


Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7

Input 2:
   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]

Output 2:
 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation

Explanation 1:
 Return the 2D array. Each row denotes the traversal of each level.



from collections import deque
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):

        result = []
        ans = []

        if A is None:
            return []

        dq = deque()
        dq.append(A)
        last = A

        while len(dq)>0:
            x= dq.popleft()
            ans.append(x)

            if A.left is not None:
                dq.append(A.left)

            if A.right is not None:
                dq.append(A.right)

            if x==last:
                result.append(ans)
                ans = []
                if len(dq)>0:
                    last = dq[-1]

        return result


