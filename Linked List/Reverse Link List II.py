Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.

Problem Constraints
1 <= |A| <= 106
1 <= B <= C <= |A|

Input Format
The first argument contains a pointer to the head of the given linked list, A.
The second arugment contains an integer, B.
The third argument contains an integer C.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 2
 C = 4

Input 2:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 1
 C = 5

Example Output
Output 1:
 1 -> 4 -> 3 -> 2 -> 5
Output 2:
 5 -> 4 -> 3 -> 2 -> 1

Example Explanation
Explanation 1:
 In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5 
 Thus, the output is 1 -> 4 -> 3 -> 2 -> 5 

Explanation 2:
 In the second example, we want to reverse the highlighted part of the given linked list : 1 -> 4 -> 3 -> 2 -> 5  
 Thus, the output is 5 -> 4 -> 3 -> 2 -> 1 



# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):  

        if A is None:
            return None
        
        if B==C:
            return A

        dummy = ListNode(0)
        dummy.next = A

        # make a dummy node before head
        leftpre = dummy
       
        # use two pointers one before reverse start element and one in the start element
        currNode = A
        for i in range(B-1):
            leftpre = leftpre.next
            currNode = currNode.next
        
        # Save the address of currNode in to a subhead for point it to last element in last
        subheadNode = currNode
        
        # start reversing the node from starting point to end
        prev = None
        for i in range(C-B+1):
            nxt = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = nxt

        # now point the leftpre to the prev that is reversed start point 
        # and our subhead to the ending element of the linked list
        leftpre.next = prev
        subheadNode.next= currNode

        return dummy.next

        
