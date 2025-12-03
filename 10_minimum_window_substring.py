"""
LeetCode 76: Minimum Window Substring

Problem:
Given two strings s and t, return the minimum window substring of s such that 
every character in t (including duplicates) is included in the window. If there 
is no such substring, return the empty string "".

Approach:
Use sliding window with two frequency maps:
1. Build frequency map for target string t
2. Expand window with right pointer until all characters are found
3. Contract window from left while maintaining validity
4. Track minimum window that contains all characters

Time Complexity: O(n + m) where n = len(s), m = len(t)
Space Complexity: O(m) for the frequency maps

Example:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window substring containing all characters of t.
        
        Args:
            s: Source string
            t: Target string with required characters
            
        Returns:
            Minimum window substring, or empty string if no such window exists
        """
        if not s or not t:
            return ""
        
        # Frequency map for target string
        target_count = Counter(t)
        required = len(target_count)  # Number of unique characters needed
        
        # Sliding window variables
        left = 0
        formed = 0  # Number of unique characters in current window with desired frequency
        window_count = {}
        
        # Result: (window length, left, right)
        result = float('inf'), None, None
        
        for right in range(len(s)):
            # Add current character to window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if current character's frequency matches target
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            # Try to contract window while it's still valid
            while left <= right and formed == required:
                char = s[left]
                
                # Update result if this window is smaller
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove leftmost character from window
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                
                left += 1
        
        # Return empty string if no valid window found
        return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]


def test_minimum_window_substring():
    """Test cases for Minimum Window Substring."""
    solution = Solution()
    
    # Test case 1: Example from problem
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    
    # Test case 2: Target is single character
    assert solution.minWindow("a", "a") == "a"
    
    # Test case 3: No valid window
    assert solution.minWindow("a", "aa") == ""
    
    # Test case 4: Entire string is the answer
    assert solution.minWindow("ab", "ab") == "ab"
    
    # Test case 5: Target at the beginning
    assert solution.minWindow("abc", "cba") == "abc"
    
    # Test case 6: Multiple valid windows
    result = solution.minWindow("ADOBECODEBANCXYZ", "ABC")
    assert result == "BANC" or result == "BECA" or len(result) == 4
    
    # Test case 7: Empty strings
    assert solution.minWindow("", "a") == ""
    assert solution.minWindow("a", "") == ""
    
    # Test case 8: Duplicates in target
    result = solution.minWindow("aaabbbcc", "abc")
    assert len(result) >= 3 and all(c in result for c in "abc")
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_minimum_window_substring()
