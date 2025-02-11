Given string A denoting an infix expression. Convert the infix expression into a postfix expression.
String A consists of ^, /, *, +, -, (, ) and lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.
Find and return the postfix expression of A.
NOTE:
^ has the highest precedence.
/ and * have equal precedence but greater than + and -.
+ and - have equal precedence and lowest precedence among given operators.

Problem Constraints
1 <= length of the string <= 500000

Input Format
The only argument given is string A.

Output Format
Return a string denoting the postfix conversion of A.

Example Input
Input 1:
 A = "x^y/(a*z)+b"

Input 2:
 A = "a+b*(c^d-e)^(f+g*h)-i"

Example Output
Output 1:
 "xy^az*/b+"
Output 2:
 "abcd^e-fgh*+^*+i-"

Example Explanation
Explanation 1:
 Ouput dentotes the postfix expression of the given input.



from collections import deque
class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        st = deque()
        A = list(A)
        result = []
        
        for i in range(len(A)):

            if A[i]  == '+':
                while len(st)>0 and st[-1] in ['+','-', '*','/','^']:
                    x = st.pop()
                    result.append(x)
                st.append(A[i])

            elif A[i] =='-':
                while len(st)>0 and st[-1] in ['-', '+','*','/','^']:
                    x = st.pop()
                    result.append(x)

                st.append(A[i])

            elif A[i] == '*':
                while len(st)>0 and st[-1] in ['*','/','^']:
                    x = st.pop()
                    result.append(x)

                st.append(A[i])

            elif A[i] == '/':
                while len(st) and st[-1] in ['/','^',"*"]:
                    x = st.pop()
                    result.append(x)

                st.append(A[i]) 

            elif A[i] =='^':
                while len(st) and st[-1] in ['^']:
                    x = st.pop()
                    result.append(x)
                st.append(A[i])


            elif A[i] == '(':
                st.append(A[i])

            elif A[i] == ')':
                while len(st) and st[-1]!= '(':
                    x = st.pop()
                    result.append(x)
                st.pop()

            else:
                result.append(A[i])


        while len(st)>0:
            result.append(st.pop())

        return "".join(result)
                
