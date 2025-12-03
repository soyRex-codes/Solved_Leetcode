"""
LeetCode 11: Container With Most Water

Problem:
You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the 
container contains the most water. Return the maximum amount of water a container can store.

Approach:
Use two pointers starting from both ends.
Calculate area = min(height[left], height[right]) * (right - left)
Move the pointer with the smaller height inward (greedy approach).
This is optimal because moving the taller pointer can only decrease the area.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only using constant extra space

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: Lines at index 1 (height=8) and index 8 (height=7) form the largest container
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find the maximum area of water that can be contained.
        
        Args:
            height: List of heights representing vertical lines
            
        Returns:
            Maximum area of water that can be contained
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer with smaller height
            # (moving the taller one can only decrease area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


def test_container_with_most_water():
    """Test cases for Container With Most Water."""
    solution = Solution()
    
    # Test case 1: Example from problem
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    # Test case 2: Two elements
    assert solution.maxArea([1, 1]) == 1
    
    # Test case 3: Increasing heights
    assert solution.maxArea([1, 2, 3, 4, 5]) == 6  # heights 1 and 5, width 4
    
    # Test case 4: Decreasing heights
    assert solution.maxArea([5, 4, 3, 2, 1]) == 6  # heights 5 and 1, width 4
    
    # Test case 5: All same height
    assert solution.maxArea([4, 4, 4, 4]) == 12  # any two with max width
    
    # Test case 6: Tall walls at ends
    assert solution.maxArea([10, 1, 1, 1, 10]) == 40  # walls at index 0 and 4
    
    # Test case 7: Single tall wall in middle
    assert solution.maxArea([1, 2, 4, 3]) == 4
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_container_with_most_water()
