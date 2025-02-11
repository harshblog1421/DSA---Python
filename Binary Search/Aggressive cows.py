Farmer John has built a new long barn with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall and an integer B which represents the number of cows.
His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the largest minimum distance possible among the cows.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 3

Input 2:
A = [1, 2]
B = 2

Example Output
Output 1:
 2

Output 2:
 1

Example Explanation
Explanation 1:
 John can assign the stalls at location 1, 3 and 5 to the 3 cows respectively. So the minimum distance will be 2.

Explanation 2:
 The minimum distance will be 1.



def no_of_possible_cows(A,n,mid):

    count = 1
    last = A[0]

    for i in range(1,len(A)):
        if A[i] - last >=mid:
            count +=1

            last = A[i]

    return count

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        
        n = len(A)
        pos = 1000000000
        for i in range(1,len(A)):
            pos = min(pos,A[i]-A[i-1])

        l = pos
        r = A[n-1] - A[0]

        while l<= r:

            mid = (l+r)//2

            if no_of_possible_cows(A,n,mid) >=B:
                ans = mid
                l = mid+1

            else:
                r = mid-1

        return ans
            
