Given a sorted linked list, delete all duplicates such that each element appears only once.

Problem Constraints
0 <= length of linked list <= 106

Input Format
First argument is the head pointer of the linked list.

Output Format
Return the head pointer of the linked list after removing all duplicates.

Example Input
Input 1:
 1->1->2

Input 2:
 1->1->2->3->3

Example Output
Output 1:
 1->2

Output 2:
 1->2->3

Example Explanation
Explanation 1:
 Each element appear only once in 1->2


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):

            prev = A
            curr = prev.next

            while curr is not None:
                if curr.val == prev.val:
                    curr = curr.next
                    continue

                prev.next = curr
                prev = curr
                curr = curr.next

            prev.next = None
            return A
