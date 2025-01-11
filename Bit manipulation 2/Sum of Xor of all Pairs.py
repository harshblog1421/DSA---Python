Given an array A of N integers. Find the sum of bitwise XOR all pairs of numbers in the array.

Since the answer can be large, return the remainder after the dividing the answer by 109+7.



Problem Constraints

1 <= N <= 105

1 <= A[i] < 109



Input Format

Only argument A is an array of integers



Output Format

Return an integer denoting the sum of xor of all pairs of number in the array.



Example Input

Input 1:
A = [1, 2, 3]
Input 2:
A = [3, 4, 2]


Example Output

Output 1:
6
Output 2:
14


Example Explanation

For Input 1:
Pair    Xor
{1, 2}  3
{1, 3}  2
{2, 3}  1
Sum of xor of all pairs = 3 + 2 + 1 = 6.
For Input 2:
Pair    Xor
{3, 4}  7
{3, 2}  1
{4, 2}  6
Sum of xor of all pairs = 7 + 1 + 6 = 14.




class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        for i in range(32):
            unset_bits = 0
            set_bits = 0
            for j in range(len(A)):
                if A[j]&(1<<i)>0:
                    set_bits+=1
                else:
                    unset_bits+=1

            possible_permutations = (set_bits*unset_bits)
            ans+=possible_permutations*(1<<i)

        return ans%(10**9+7)
