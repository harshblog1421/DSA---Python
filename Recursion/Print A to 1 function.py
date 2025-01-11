You are given an integer A, print A to 1 using using recursion.

Note :- After printing all the numbers from A to 1, print a new line.


import sys
sys.setrecursionlimit(10**6)

def printnto1(A):
    if A ==0:
        return 
    print(A,end = ' ')
    printnto1(A-1)
class Solution:
    # @param A : integer
    def solve(self, A):
        printnto1(A)
        print(end= '\n')
        
