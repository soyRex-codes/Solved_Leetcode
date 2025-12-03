"""
LeetCode 3: Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Approach:
Use sliding window with a hash set to track characters in the current window.
Expand the window by moving right pointer and adding characters to set.
When a duplicate is found, shrink the window from the left until the duplicate is removed.
Track the maximum window size seen.

Time Complexity: O(n) - each character is visited at most twice (once by right, once by left)
Space Complexity: O(min(n, m)) where n is string length and m is charset size

Example:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        
        Args:
            s: Input string
            
        Returns:
            Length of the longest substring without repeating characters
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Shrink window from left while we have duplicates
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to set
            char_set.add(s[right])
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def lengthOfLongestSubstringOptimized(self, s: str) -> int:
        """
        Optimized version using hash map to store character indices.
        
        Args:
            s: Input string
            
        Returns:
            Length of the longest substring without repeating characters
        """
        char_index = {}  # Maps character to its most recent index
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If character is already in current window, move left pointer
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            
            # Update character's latest index
            char_index[s[right]] = right
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length


def test_longest_substring_without_repeating():
    """Test cases for Longest Substring Without Repeating Characters."""
    solution = Solution()
    
    # Test case 1: Example from problem
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    
    # Test case 2: All same characters
    assert solution.lengthOfLongestSubstring("bbbbb") == 1  # "b"
    
    # Test case 3: Longer substring
    assert solution.lengthOfLongestSubstring("pwwkew") == 3  # "wke"
    
    # Test case 4: Empty string
    assert solution.lengthOfLongestSubstring("") == 0
    
    # Test case 5: All unique
    assert solution.lengthOfLongestSubstring("abcdef") == 6
    
    # Test case 6: Single character
    assert solution.lengthOfLongestSubstring("a") == 1
    
    # Test case 7: Spaces and special characters
    assert solution.lengthOfLongestSubstring("a b c a b c") == 3  # " bc"
    
    # Test optimized version
    assert solution.lengthOfLongestSubstringOptimized("abcabcbb") == 3
    assert solution.lengthOfLongestSubstringOptimized("pwwkew") == 3
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_substring_without_repeating()
