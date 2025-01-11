Given an array of integers, every element appears thrice except for one, which occurs once.

Find that element that does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
		B= 0
		for i in range(32):

			count = 0
			for j in range(len(A)):
				if A[j]&(1<<i)>0:
					count +=1

			if count%3>0:
					B = B|(1<<i)

		return B
