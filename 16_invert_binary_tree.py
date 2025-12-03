"""
LeetCode 226: Invert Binary Tree

Problem:
Given the root of a binary tree, invert the tree, and return its root.
Inverting means swapping the left and right children of all nodes.

Approach:
Use recursive DFS to traverse the tree.
For each node, swap its left and right children.
Recursively invert left and right subtrees.

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion stack where h is tree height (O(n) worst case)

Example:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree recursively.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Root of the inverted tree
        """
        # Base case
        if not root:
            return None
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree iteratively using BFS.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Root of the inverted tree
        
        Time Complexity: O(n)
        Space Complexity: O(n) - queue can hold up to n/2 nodes at the last level
        """
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Swap children
            node.left, node.right = node.right, node.left
            
            # Add children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root


def tree_to_list(root):
    """Helper function to convert tree to list (level order) for testing."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def list_to_tree(values):
    """Helper function to create tree from level order list."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def test_invert_binary_tree():
    """Test cases for Invert Binary Tree."""
    solution = Solution()
    
    # Test case 1: Example from problem
    root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]
    
    # Test case 2: Single node
    root = list_to_tree([1])
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [1]
    
    # Test case 3: Empty tree
    assert solution.invertTree(None) is None
    
    # Test case 4: Unbalanced tree
    root = list_to_tree([1, 2, None, 3])
    inverted = solution.invertTree(root)
    assert tree_to_list(inverted) == [1, None, 2, None, 3]
    
    # Test iterative version
    root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    inverted = solution.invertTreeIterative(root)
    assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_invert_binary_tree()
