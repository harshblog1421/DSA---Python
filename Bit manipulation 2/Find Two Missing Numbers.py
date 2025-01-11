Given an array A of length N where all the elements are distinct and are in the range [1, N+2].

Two numbers from the range [1, N+2] are missing from the array A. Find the two missing numbers.



Problem Constraints

1 <= N <= 105

1 <= A[i] <= N+2

The elements of array A are distinct



Input Format

Only argument A is an array of integers



Output Format

Return a sorted array of size 2 denoting the missing elements.



Example Input

Input 1:
A = [3, 2, 4]
Input 2:
A = [5, 1, 3, 6]


Example Output

Output 1:
[1, 5]
Output 2:
[2, 4]


Example Explanation

For Input 1:
The missing numbers are 1 and 5.
For Input 2:
The missing numbers are 2 and 4.


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #x + y = (x ^ y) + 2 * (x & y)
        #from above formula we need have x&y as zero result wen need to get x^y, for this x bit should be oppsoite of y bits 
        # x = 101 , value of y should be 010
        n=A
        #please assign a to n bcoz A should remain for later part of the code
        count=0

        #count number of bit positions for given A
        while n>0:
            count+=1
            n = n>>1

        #get the new valuex=0  by setting 0's poisiont of A to 1's
        x=0
        for i in range(count):
            if ( A & (1 << i) ) == 0:
                x = x | (1 << i)

       #y will be very next 2**i value,so do leftshift on 1 ro get that value of (10 or 100 or 1000 or 1000 ...... and so on)         
        y = 1<<count

        #Now x is a value which is just greatest number smaller than A 
        #y is value which is 
        #return the final output
        return x ^ y
