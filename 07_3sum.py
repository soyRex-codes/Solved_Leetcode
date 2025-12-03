"""
LeetCode 15: 3Sum

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Approach:
1. Sort the array
2. For each element, use two pointers to find pairs that sum to the negative of that element
3. Skip duplicates to avoid duplicate triplets

Time Complexity: O(n²) - O(n log n) for sorting + O(n²) for nested iterations
Space Complexity: O(1) or O(n) depending on sorting algorithm (excluding output)

Example:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets that sum to zero.
        
        Args:
            nums: List of integers
            
        Returns:
            List of triplets that sum to zero
        """
        result = []
        nums.sort()  # Sort the array
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers approach
            left = i + 1
            right = n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result


def test_three_sum():
    """Test cases for 3Sum."""
    solution = Solution()
    
    # Test case 1: Multiple triplets
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result) == sorted(expected)
    
    # Test case 2: No triplets
    assert solution.threeSum([1, 2, 3]) == []
    
    # Test case 3: All zeros
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
    
    # Test case 4: Empty array
    assert solution.threeSum([]) == []
    
    # Test case 5: Two elements
    assert solution.threeSum([0, 1]) == []
    
    # Test case 6: Multiple duplicates
    result = solution.threeSum([0, 0, 0, 0])
    assert result == [[0, 0, 0]]
    
    # Test case 7: Mix of positive and negative
    result = solution.threeSum([-2, 0, 1, 1, 2])
    expected = [[-2, 0, 2], [-2, 1, 1]]
    assert sorted(result) == sorted(expected)
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_three_sum()
