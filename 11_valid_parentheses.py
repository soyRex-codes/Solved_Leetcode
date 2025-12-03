"""
LeetCode 20: Valid Parentheses

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Approach:
Use a stack to track opening brackets.
For each closing bracket, check if it matches the most recent opening bracket.
If the stack is empty when we need to match, or if brackets don't match, it's invalid.

Time Complexity: O(n) - single pass through the string
Space Complexity: O(n) - stack can store at most n/2 opening brackets

Example:
    Input: s = "()[]{}"
    Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if the parentheses string is valid.
        
        Args:
            s: String containing brackets
            
        Returns:
            True if brackets are valid and properly matched, False otherwise
        """
        # Map closing brackets to their opening counterparts
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for char in s:
            if char in bracket_map:
                # It's a closing bracket
                # Check if stack is not empty and top matches
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
        
        # Valid only if stack is empty (all brackets matched)
        return len(stack) == 0


def test_valid_parentheses():
    """Test cases for Valid Parentheses."""
    solution = Solution()
    
    # Test case 1: Simple valid case
    assert solution.isValid("()") == True
    
    # Test case 2: Multiple types
    assert solution.isValid("()[]{}") == True
    
    # Test case 3: Invalid - wrong order
    assert solution.isValid("(]") == False
    
    # Test case 4: Nested brackets
    assert solution.isValid("([{}])") == True
    
    # Test case 5: Invalid - not closed
    assert solution.isValid("(") == False
    
    # Test case 6: Invalid - only closing
    assert solution.isValid(")") == False
    
    # Test case 7: Complex nested
    assert solution.isValid("{[()]}") == True
    
    # Test case 8: Invalid - mismatched
    assert solution.isValid("([)]") == False
    
    # Test case 9: Empty string
    assert solution.isValid("") == True
    
    # Test case 10: Multiple same type
    assert solution.isValid("((()))") == True
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_valid_parentheses()
