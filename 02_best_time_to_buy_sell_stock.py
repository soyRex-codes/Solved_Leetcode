"""
LeetCode 121: Best Time to Buy and Sell Stock

Problem:
You are given an array prices where prices[i] is the price of a given stock on 
the ith day. You want to maximize your profit by choosing a single day to buy 
one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

Approach:
Track the minimum price seen so far as we iterate through the array.
For each price, calculate the profit if we sold at this price (current - min_price).
Keep track of the maximum profit seen.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only using constant extra space

Example:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum profit from buying and selling stock once.
        
        Args:
            prices: List of stock prices where prices[i] is price on day i
            
        Returns:
            Maximum profit achievable, or 0 if no profit is possible
        """
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum price seen so far
            min_price = min(min_price, price)
            
            # Calculate profit if we sell at current price
            current_profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, current_profit)
        
        return max_profit


def test_best_time_to_buy_sell_stock():
    """Test cases for Best Time to Buy and Sell Stock."""
    solution = Solution()
    
    # Test case 1: Example from problem
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    
    # Test case 2: Decreasing prices (no profit)
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    
    # Test case 3: Single day
    assert solution.maxProfit([5]) == 0
    
    # Test case 4: Two days with profit
    assert solution.maxProfit([1, 2]) == 1
    
    # Test case 5: Maximum profit at the end
    assert solution.maxProfit([2, 4, 1, 7]) == 6
    
    # Test case 6: Empty array
    assert solution.maxProfit([]) == 0
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_best_time_to_buy_sell_stock()
