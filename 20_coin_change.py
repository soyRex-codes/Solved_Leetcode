"""
LeetCode 322: Coin Change

Problem:
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money. Return the fewest 
number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Approach:
Use bottom-up Dynamic Programming:
- dp[i] = minimum coins needed to make amount i
- For each amount, try all coins and take minimum
- dp[amount] = min(dp[amount - coin] + 1) for all coins

Time Complexity: O(amount × n) where n is number of coins
Space Complexity: O(amount) for DP array

Example:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Find minimum number of coins needed to make the amount.
        
        Args:
            coins: List of coin denominations
            amount: Target amount
            
        Returns:
            Minimum number of coins needed, or -1 if impossible
        """
        # Initialize DP array
        # dp[i] represents minimum coins needed for amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        # Build up DP table
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    # Try using this coin
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return result (-1 if impossible)
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def coinChangeRecursiveMemo(self, coins: List[int], amount: int) -> int:
        """
        Top-down DP solution with memoization.
        
        Args:
            coins: List of coin denominations
            amount: Target amount
            
        Returns:
            Minimum number of coins needed, or -1 if impossible
        
        Time Complexity: O(amount × n)
        Space Complexity: O(amount) - memo + recursion stack
        """
        memo = {}
        
        def min_coins(remaining):
            # Base cases
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            # Check memo
            if remaining in memo:
                return memo[remaining]
            
            # Try all coins
            min_count = float('inf')
            for coin in coins:
                result = min_coins(remaining - coin)
                if result != float('inf'):
                    min_count = min(min_count, result + 1)
            
            memo[remaining] = min_count
            return min_count
        
        result = min_coins(amount)
        return result if result != float('inf') else -1
    
    def coinChangeBFS(self, coins: List[int], amount: int) -> int:
        """
        BFS approach (useful for understanding, but less efficient).
        
        Args:
            coins: List of coin denominations
            amount: Target amount
            
        Returns:
            Minimum number of coins needed, or -1 if impossible
        
        Time Complexity: O(amount × n)
        Space Complexity: O(amount)
        """
        if amount == 0:
            return 0
        
        from collections import deque
        
        queue = deque([(0, 0)])  # (current_amount, coin_count)
        visited = {0}
        
        while queue:
            current_amount, coin_count = queue.popleft()
            
            for coin in coins:
                next_amount = current_amount + coin
                
                if next_amount == amount:
                    return coin_count + 1
                
                if next_amount < amount and next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, coin_count + 1))
        
        return -1


def test_coin_change():
    """Test cases for Coin Change."""
    solution = Solution()
    
    # Test case 1: Example from problem
    assert solution.coinChange([1, 2, 5], 11) == 3  # 5+5+1
    
    # Test case 2: Impossible case
    assert solution.coinChange([2], 3) == -1
    
    # Test case 3: Amount is 0
    assert solution.coinChange([1], 0) == 0
    
    # Test case 4: Single coin matches
    assert solution.coinChange([1, 2, 5], 5) == 1
    
    # Test case 5: Need multiple coins
    assert solution.coinChange([1, 3, 4], 6) == 2  # 3+3
    
    # Test case 6: Large amount
    assert solution.coinChange([1, 2, 5], 100) == 20  # 20 coins of 5
    
    # Test case 7: Only one coin type
    assert solution.coinChange([1], 7) == 7
    
    # Test case 8: Greedy doesn't work
    assert solution.coinChange([1, 3, 4], 6) == 2  # 3+3, not 4+1+1
    
    # Test recursive with memoization
    assert solution.coinChangeRecursiveMemo([1, 2, 5], 11) == 3
    assert solution.coinChangeRecursiveMemo([2], 3) == -1
    
    # Test BFS approach (on smaller inputs)
    assert solution.coinChangeBFS([1, 2, 5], 11) == 3
    assert solution.coinChangeBFS([2], 3) == -1
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_coin_change()
