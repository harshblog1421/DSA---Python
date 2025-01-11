Given a number A, we need to find the sum of its digits using recursion.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        
        return A % 10 + self.solve(A // 10)
