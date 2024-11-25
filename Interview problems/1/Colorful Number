Given a number A, find if it is COLORFUL number or not.

If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:

A number can be broken into different consecutive sequence of digits. 
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
This number is a COLORFUL number, since the product of every consecutive sequence of digits is different

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)  # Convert number to string for easier manipulation
        product_set = set()  # Set to store products of digit subsequences

        # Traverse through all subsequences of digits
        for i in range(len(A)):
            product = 1
            for j in range(i, len(A)):
                product *= int(A[j])  # Calculate product of digits in the subsequence
                if product in product_set:
                    return 0  # If product repeats, return 0 (not colorful)
                product_set.add(product)

        return 1  # If no repeated product, return 1 (colorful number)
