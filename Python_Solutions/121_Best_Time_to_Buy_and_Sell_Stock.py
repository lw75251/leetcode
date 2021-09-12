class Solution:
    """
    My Solution: Brute Force O(n^2)

    IDEA: Try all the combinations, and replace the max profit
    if we find something larger.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = max(prices[j] - prices[i], max_profit)
        return max_profit

    """
    My Solution 2: Iterate Backwards O(n)
    
    IDEA: Start backwards, since you can only sell a stock in the future.
    Apply a greedy method, where we keep the max price and try all
    possible profits, saving the maximum.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        profits = 0
        for p in reversed(prices):
            max_price = max(p, max_price)
            profits = max(max_price - p, profits)
        return profits
