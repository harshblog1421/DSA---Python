An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each string may be an integer or an operator.
Note: Reverse Polish Notation is equivalent to Postfix Expression, where operators are written after their operands.

Problem Constraints
1 <= N <= 105

Input Format
The only argument given is string array A.

Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.

Example Input
Input 1:
A =   ["2", "1", "+", "3", "*"]

Input 2:
A = ["4", "13", "5", "/", "+"]

Example Output
Output 1:
9
Output 2:
6

Example Explanation
Explaination 1:
starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9
Explaination 2:
starting from backside:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    13 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6



from collections import deque

class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):

        stack = deque()
        for i in range(len(A)):
            if A[i] in ('*','+','/','-','//'):
                first_no = stack.pop()
                second_no = stack.pop()

                if A[i] == '*':
                    stack.append(first_no * second_no)

                elif A[i] == '-':
                    stack.append(second_no - first_no)

                elif A[i] == '/' or A[i] =='//':
                    stack.append(second_no// first_no)

                elif A[i] =='+':
                    stack.append(first_no + second_no)

            else:
                stack.append(int(A[i]))

        return stack.pop()
