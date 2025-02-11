Given two strings A and B. Each string represents an expression consisting of lowercase English alphabets, '+', '-', '(' and ')'.
The task is to compare them and check if they are similar. If they are identical, return 1 else, return 0.
NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’, and every operand appears only once.

Problem Constraints
1 <= length of the each String <= 100

Input Format
The given arguments are string A and string B.

Output Format
Return 1 if they represent the same expression else return 0.
  
Example Input
Input 1:
 A = "-(a+b+c)"
 B = "-a-b-c"

Input 2:
 A = "a-b-(c-d)"
 B = "a-b-c-d"

Example Output
Output 1:
 1

Output 2:
 0

Example Explanation
Explanation 1:
 The expression "-(a+b+c)" can be written as "-a-b-c" which is equal as B. 

Explanation 2:
 Both the expression are different.



  from collections import deque

def process(expr):
    stack = [1]
    sign = 1
    result = {}
    i = 0
    while i<len(expr):
        if expr[i] =="+":
            sign = stack[-1]

        elif expr[i] =='-':
            sign = -stack[-1]

        elif expr[i] == '(':
            stack.append(sign)

        elif expr[i] == ')':
            stack.pop()

        elif 'a' <= expr[i] <= 'z':
            
            if expr[i] in result:
                result[expr[i]] += sign
            
            else:
                result[expr[i]]= sign
        
        i+=1
    return result

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        normalized_A = process(A)
        normalized_B = process(B)
        return 1 if normalized_A == normalized_B else 0
