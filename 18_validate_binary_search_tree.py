"""
LeetCode 98: Validate Binary Search Tree

Problem:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Approach 1 (Range Validation):
Pass valid range (min, max) down the tree recursively.
Each node must be within its valid range.

Approach 2 (In-order Traversal):
Perform in-order traversal - should produce sorted sequence for valid BST.

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion stack

Example:
    Input: root = [2,1,3]
    Output: true
"""

from typing import Optional
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validate BST using range validation approach.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            True if tree is a valid BST, False otherwise
        """
        def validate(node, min_val, max_val):
            # Empty tree is valid
            if not node:
                return True
            
            # Check if current node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees with updated ranges
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
    
    def isValidBSTInorder(self, root: Optional[TreeNode]) -> bool:
        """
        Validate BST using in-order traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            True if tree is a valid BST, False otherwise
        """
        self.prev = None
        
        def inorder(node):
            if not node:
                return True
            
            # Check left subtree
            if not inorder(node.left):
                return False
            
            # Check current node
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            
            # Check right subtree
            return inorder(node.right)
        
        return inorder(root)
    
    def isValidBSTIterative(self, root: Optional[TreeNode]) -> bool:
        """
        Validate BST using iterative in-order traversal.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            True if tree is a valid BST, False otherwise
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        stack = []
        prev = None
        current = root
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            
            # Check BST property
            if prev is not None and current.val <= prev:
                return False
            prev = current.val
            
            # Move to right subtree
            current = current.right
        
        return True


def list_to_tree(values):
    """Helper function to create tree from level order list."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def test_validate_binary_search_tree():
    """Test cases for Validate Binary Search Tree."""
    solution = Solution()
    
    # Test case 1: Valid BST
    root = list_to_tree([2, 1, 3])
    assert solution.isValidBST(root) == True
    
    # Test case 2: Invalid BST (right child violation)
    root = list_to_tree([5, 1, 4, None, None, 3, 6])
    assert solution.isValidBST(root) == False
    
    # Test case 3: Single node
    root = list_to_tree([1])
    assert solution.isValidBST(root) == True
    
    # Test case 4: Empty tree
    assert solution.isValidBST(None) == True
    
    # Test case 5: Left-skewed valid BST
    root = list_to_tree([3, 2, None, 1])
    assert solution.isValidBST(root) == True
    
    # Test case 6: Two nodes
    root = list_to_tree([1, 1])
    assert solution.isValidBST(root) == False  # Duplicate values not allowed
    
    # Test case 7: Complex invalid case
    root = list_to_tree([5, 4, 6, None, None, 3, 7])
    assert solution.isValidBST(root) == False  # 3 is less than 5
    
    # Test in-order approach
    root = list_to_tree([2, 1, 3])
    assert solution.isValidBSTInorder(root) == True
    
    # Test iterative approach
    root = list_to_tree([2, 1, 3])
    assert solution.isValidBSTIterative(root) == True
    
    root = list_to_tree([5, 1, 4, None, None, 3, 6])
    assert solution.isValidBSTIterative(root) == False
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_validate_binary_search_tree()
