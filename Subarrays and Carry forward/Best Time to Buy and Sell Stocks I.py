Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Return the maximum possible profit.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)

        # If there are less than two days, no profit can be made
        if n < 2:
            return 0
        
        max_value = A[n-1]  # Start with the last element as the maximum value
        max_profit = 0
        profit = 0

        # Traverse the array from the second-last day to the first
        for i in range(n-2, -1, -1):
            if A[i] > max_value:
                # Update the max_value if we find a higher value
                max_value = A[i]
            else:
                # Calculate profit by selling at max_value and buying at A[i]
                profit = max_value - A[i]
                # Update the maximum profit
                max_profit = max(max_profit, profit)

        return max_profit
