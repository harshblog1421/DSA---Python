You are given a linked list A
Each node in the linked list contains two pointers: a next pointer and a random pointer
The next pointer points to the next node in the list
The random pointer can point to any node in the list, or it can be NULL
Your task is to create a deep copy of the linked list A
The copied list should be a completely separate linked list from the original list, but with the same node values and random pointer connections as the original list
You should create a new linked list B, where each node in B has the same value as the corresponding node in A
The next and random pointers of each node in B should point to the corresponding nodes in B (rather than A)

Problem Constraints
0 <= |A| <= 106

Input Format
The first argument of input contains a pointer to the head of linked list A.

Output Format
Return a pointer to the head of the required linked list.

Example Input
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  
Example Output
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        
        #step1 = make extra nodes inbetween the nodes of our list
        if head is None:
            return None

        temp = head
        while temp is not None:
            nxt = temp.next
            temp.next = RandomListNode(temp.label)
            temp.next.next = nxt
            temp = temp.next.next

        
        #step2  = connect the random nodes in the copied version
        temp = head
        while temp is not None:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # step3  = split the lists into single single
        temp = head
        head2 = temp.next
        copy = head2

        while temp is not None:
            temp.next = temp.next.next 
            copy.next = copy.next.next if copy.next is not None else None
            temp = temp.next
            copy = copy.next

        return head2
