"""
LeetCode 1: Two Sum

Problem:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target. You may assume that each input 
would have exactly one solution, and you may not use the same element twice.

Approach:
Use a hash map to store each number and its index as we iterate through the array.
For each number, check if (target - current_number) exists in the hash map.
If it does, we've found our pair. If not, add the current number to the hash map.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map stores at most n elements

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1]
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to the target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of the two numbers that add up to target
        """
        # Hash map to store {number: index}
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our hash map
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # Should never reach here based on problem constraints
        return []


def test_two_sum():
    """Test cases for Two Sum problem."""
    solution = Solution()
    
    # Test case 1: Basic example
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2: Answer at the end
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3: Two elements
    assert solution.twoSum([3, 3], 6) == [0, 1]
    
    # Test case 4: Negative numbers
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    
    # Test case 5: Mix of positive and negative
    assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_two_sum()
