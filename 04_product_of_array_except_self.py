"""
LeetCode 238: Product of Array Except Self

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.

Approach:
Use two passes:
1. Left pass: Calculate prefix products (product of all elements to the left)
2. Right pass: Calculate suffix products (product of all elements to the right)
   and multiply with prefix products

For each position i:
answer[i] = (product of all elements left of i) * (product of all elements right of i)

Time Complexity: O(n) - two passes through the array
Space Complexity: O(1) - excluding the output array (which doesn't count per problem)

Example:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Explanation: 
        answer[0] = 2*3*4 = 24
        answer[1] = 1*3*4 = 12
        answer[2] = 1*2*4 = 8
        answer[3] = 1*2*3 = 6
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate product of array except self without division.
        
        Args:
            nums: List of integers
            
        Returns:
            List where each element is the product of all other elements
        """
        n = len(nums)
        result = [1] * n
        
        # Left pass: Calculate prefix products
        # result[i] will contain the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Right pass: Multiply with suffix products
        # Multiply result[i] with product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result


def test_product_except_self():
    """Test cases for Product of Array Except Self."""
    solution = Solution()
    
    # Test case 1: Basic example
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    # Test case 2: With zeros
    assert solution.productExceptSelf([0, 0]) == [0, 0]
    
    # Test case 3: Single zero
    assert solution.productExceptSelf([1, 2, 0, 4]) == [0, 0, 8, 0]
    
    # Test case 4: Negative numbers
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    
    # Test case 5: All ones
    assert solution.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]
    
    # Test case 6: Two elements
    assert solution.productExceptSelf([3, 4]) == [4, 3]
    
    # Test case 7: Mix of positive and negative
    assert solution.productExceptSelf([2, -3, 4]) == [-12, 8, -6]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_product_except_self()
