Given a linked list A, remove the B-th node from the end of the list and return its head.
For example, given linked list: 1->2->3->4->5, and B = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
NOTE: If B is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.

Problem Constraints
1 <= |A| <= 10^6

Input Format
The first argument of input contains a pointer to the head of the linked list. The second argument of input contains the integer B.

Output Format
Return the head of the linked list after deleting the B-th element from the end.

Example Input
Input 1:
A = 1->2->3->4->5
B = 2

Input 2:
A = 1
B = 1

Example Output
Output 1:
1->2->3->5

Output 2:  
Example Explanation
Explanation 1:
In the first example, 4 is the second last element.
Explanation 2:
In the second example, 1 is the first and the last element.



  # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):

            temp = A

            count =0
            temp = A
            while temp is not None:
                temp = temp.next
                count +=1     

            if count -B ==0:
                return A.next

            if B==1:
                temp = A
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
                return A

            if count<B:
                return A.next

            temp = A
            position = 0
            while temp is not None and position< count-B-1:
                position+=1
                temp = temp.next

            temp.next = temp.next.next

            return A


            
