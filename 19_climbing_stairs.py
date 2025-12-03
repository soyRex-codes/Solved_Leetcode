"""
LeetCode 70: Climbing Stairs

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you 
climb to the top?

Approach:
This is a Fibonacci problem!
- To reach step n, you can come from step (n-1) or step (n-2)
- So: ways(n) = ways(n-1) + ways(n-2)
- Base cases: ways(1) = 1, ways(2) = 2

Optimized using constant space by keeping only last two values.

Time Complexity: O(n) - compute each step once
Space Complexity: O(1) - only storing two variables

Example:
    Input: n = 3
    Output: 3
    Explanation: There are three ways: 1+1+1, 1+2, 2+1
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate number of ways to climb n stairs.
        
        Args:
            n: Number of stairs
            
        Returns:
            Number of distinct ways to climb to the top
        """
        if n <= 2:
            return n
        
        # Initialize base cases
        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2
        
        # Calculate iteratively using Fibonacci pattern
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    def climbStairsDP(self, n: int) -> int:
        """
        Solution using DP array (less space efficient but clearer).
        
        Args:
            n: Number of stairs
            
        Returns:
            Number of distinct ways to climb to the top
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def climbStairsRecursiveMemo(self, n: int) -> int:
        """
        Recursive solution with memoization (top-down DP).
        
        Args:
            n: Number of stairs
            
        Returns:
            Number of distinct ways to climb to the top
        
        Time Complexity: O(n)
        Space Complexity: O(n) - recursion stack + memo
        """
        memo = {}
        
        def climb(step):
            if step <= 2:
                return step
            
            if step in memo:
                return memo[step]
            
            memo[step] = climb(step - 1) + climb(step - 2)
            return memo[step]
        
        return climb(n)


def test_climbing_stairs():
    """Test cases for Climbing Stairs."""
    solution = Solution()
    
    # Test case 1: Small example
    assert solution.climbStairs(2) == 2
    
    # Test case 2: Example from problem
    assert solution.climbStairs(3) == 3
    
    # Test case 3: Larger number
    assert solution.climbStairs(5) == 8
    
    # Test case 4: Base case
    assert solution.climbStairs(1) == 1
    
    # Test case 5: Larger value
    assert solution.climbStairs(10) == 89
    
    # Test case 6: Even larger
    assert solution.climbStairs(20) == 10946
    
    # Test DP array approach
    assert solution.climbStairsDP(3) == 3
    assert solution.climbStairsDP(5) == 8
    
    # Test recursive with memoization
    assert solution.climbStairsRecursiveMemo(3) == 3
    assert solution.climbStairsRecursiveMemo(10) == 89
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_climbing_stairs()
