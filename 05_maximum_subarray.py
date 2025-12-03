"""
LeetCode 53: Maximum Subarray

Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Approach:
Use Kadane's Algorithm:
- Keep track of the maximum sum ending at the current position
- At each position, decide whether to extend the existing subarray or start a new one
- Choose the maximum between: (current_element) vs (current_element + previous_sum)
- Track the global maximum throughout

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only using constant extra space

Example:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray with the largest sum using Kadane's algorithm.
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum sum of any contiguous subarray
        """
        if not nums:
            return 0
        
        # Initialize with the first element
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate through the rest of the array
        for i in range(1, len(nums)):
            # Either extend existing subarray or start new one
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update global maximum
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    def maxSubArrayWithIndices(self, nums: List[int]) -> tuple:
        """
        Find maximum subarray and return (max_sum, start_index, end_index).
        
        Args:
            nums: List of integers
            
        Returns:
            Tuple of (maximum sum, start index, end index)
        """
        if not nums:
            return (0, 0, 0)
        
        current_sum = nums[0]
        max_sum = nums[0]
        
        start = 0
        end = 0
        temp_start = 0
        
        for i in range(1, len(nums)):
            # If starting fresh is better, update temp_start
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
                temp_start = i
            else:
                current_sum = current_sum + nums[i]
            
            # Update max_sum and indices if we found a new maximum
            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i
        
        return (max_sum, start, end)


def test_maximum_subarray():
    """Test cases for Maximum Subarray."""
    solution = Solution()
    
    # Test case 1: Mixed positive and negative
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    
    # Test case 2: All positive
    assert solution.maxSubArray([1, 2, 3, 4, 5]) == 15
    
    # Test case 3: All negative
    assert solution.maxSubArray([-5, -2, -8, -1]) == -1
    
    # Test case 4: Single element
    assert solution.maxSubArray([5]) == 5
    assert solution.maxSubArray([-3]) == -3
    
    # Test case 5: Two elements
    assert solution.maxSubArray([5, 4]) == 9
    assert solution.maxSubArray([-1, -2]) == -1
    
    # Test case 6: Zeros included
    assert solution.maxSubArray([0, -3, 1, 1]) == 2
    
    # Test with indices
    result = solution.maxSubArrayWithIndices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert result[0] == 6  # max sum
    assert result[1] == 3  # start index
    assert result[2] == 6  # end index
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_maximum_subarray()
