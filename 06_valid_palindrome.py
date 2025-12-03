"""
LeetCode 125: Valid Palindrome

Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward 
and backward. Given a string s, return true if it is a palindrome, or false otherwise.

Approach:
Use two pointers starting from both ends of the string.
Skip non-alphanumeric characters and compare characters in lowercase.
Move pointers toward each other until they meet.

Time Complexity: O(n) - single pass through the string
Space Complexity: O(1) - only using constant extra space

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if string is a valid palindrome ignoring non-alphanumeric characters.
        
        Args:
            s: Input string
            
        Returns:
            True if the string is a palindrome, False otherwise
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    def isPalindromeAlternative(self, s: str) -> bool:
        """
        Alternative solution using string filtering.
        
        Args:
            s: Input string
            
        Returns:
            True if the string is a palindrome, False otherwise
        """
        # Filter and normalize the string
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        
        # Check if it's the same as its reverse
        return filtered == filtered[::-1]


def test_valid_palindrome():
    """Test cases for Valid Palindrome."""
    solution = Solution()
    
    # Test case 1: Valid palindrome with spaces and punctuation
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    
    # Test case 2: Not a palindrome
    assert solution.isPalindrome("race a car") == False
    
    # Test case 3: Empty string
    assert solution.isPalindrome(" ") == True
    
    # Test case 4: Single character
    assert solution.isPalindrome("a") == True
    
    # Test case 5: Only non-alphanumeric
    assert solution.isPalindrome(".,") == True
    
    # Test case 6: Numbers included
    assert solution.isPalindrome("0P") == False
    assert solution.isPalindrome("1a2") == False
    
    # Test alternative solution
    assert solution.isPalindromeAlternative("A man, a plan, a canal: Panama") == True
    assert solution.isPalindromeAlternative("race a car") == False
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_valid_palindrome()
