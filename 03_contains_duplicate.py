"""
LeetCode 217: Contains Duplicate

Problem:
Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Approach:
Use a hash set to track numbers we've seen. As we iterate through the array,
if we encounter a number already in the set, we've found a duplicate.
If we complete the iteration without finding duplicates, all elements are unique.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash set stores at most n elements

Example:
    Input: nums = [1,2,3,1]
    Output: true
    Explanation: The element 1 appears twice
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the array contains any duplicates.
        
        Args:
            nums: List of integers
            
        Returns:
            True if any value appears at least twice, False otherwise
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
    
    def containsDuplicateAlternative(self, nums: List[int]) -> bool:
        """
        Alternative solution using set length comparison.
        
        Args:
            nums: List of integers
            
        Returns:
            True if any value appears at least twice, False otherwise
        """
        return len(nums) != len(set(nums))


def test_contains_duplicate():
    """Test cases for Contains Duplicate."""
    solution = Solution()
    
    # Test case 1: Has duplicates
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    
    # Test case 2: All unique
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    
    # Test case 3: Multiple duplicates
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    
    # Test case 4: Single element
    assert solution.containsDuplicate([1]) == False
    
    # Test case 5: Empty array
    assert solution.containsDuplicate([]) == False
    
    # Test case 6: Negative numbers with duplicates
    assert solution.containsDuplicate([-1, -2, -3, -1]) == True
    
    # Test alternative solution
    assert solution.containsDuplicateAlternative([1, 2, 3, 1]) == True
    assert solution.containsDuplicateAlternative([1, 2, 3, 4]) == False
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_contains_duplicate()
