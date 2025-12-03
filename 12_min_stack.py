"""
LeetCode 155: Min Stack

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element 
in constant time. Implement the MinStack class with:
- push(val): Push the element val onto the stack
- pop(): Remove the element on the top of the stack
- top(): Get the top element of the stack
- getMin(): Retrieve the minimum element in the stack

All operations must run in O(1) time.

Approach:
Use two stacks:
1. Main stack: stores all elements
2. Min stack: stores minimum values (synchronized with main stack)

When pushing, push to both stacks (min stack gets min(val, current_min))
When popping, pop from both stacks

Time Complexity: O(1) for all operations
Space Complexity: O(n) - two stacks of size n

Example:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()  # returns -3
    minStack.pop()
    minStack.top()     # returns 0
    minStack.getMin()  # returns -2
"""


class MinStack:
    def __init__(self):
        """Initialize the stack data structures."""
        self.stack = []      # Main stack
        self.min_stack = []  # Stack to track minimums
    
    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        
        Args:
            val: Value to push
        """
        self.stack.append(val)
        
        # Push minimum value onto min_stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
    
    def pop(self) -> None:
        """Remove the element on the top of the stack."""
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        """
        Get the top element of the stack.
        
        Returns:
            Top element value
        """
        return self.stack[-1]
    
    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        
        Returns:
            Minimum element value
        """
        return self.min_stack[-1]


class MinStackOptimized:
    """
    Optimized version that only stores minimum when it changes.
    Uses less space on average but same O(n) worst case.
    """
    
    def __init__(self):
        """Initialize the stack data structures."""
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        """Push element val onto stack."""
        self.stack.append(val)
        
        # Only push to min_stack if it's a new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        """Remove the element on the top of the stack."""
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    
    def top(self) -> int:
        """Get the top element of the stack."""
        return self.stack[-1]
    
    def getMin(self) -> int:
        """Retrieve the minimum element in the stack."""
        return self.min_stack[-1]


def test_min_stack():
    """Test cases for Min Stack."""
    # Test basic MinStack
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
    
    # Test with all same values
    min_stack2 = MinStack()
    min_stack2.push(5)
    min_stack2.push(5)
    min_stack2.push(5)
    assert min_stack2.getMin() == 5
    min_stack2.pop()
    assert min_stack2.getMin() == 5
    
    # Test optimized version
    min_stack3 = MinStackOptimized()
    min_stack3.push(1)
    min_stack3.push(2)
    min_stack3.push(0)
    assert min_stack3.getMin() == 0
    min_stack3.pop()
    assert min_stack3.getMin() == 1
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_min_stack()
