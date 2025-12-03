"""
LeetCode 104: Maximum Depth of Binary Tree

Problem:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Approach:
Use recursive DFS:
- Base case: empty tree has depth 0
- Recursive case: depth = 1 + max(left_depth, right_depth)

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion stack where h is tree height

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth of a binary tree using DFS.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Maximum depth of the tree
        """
        # Base case: empty tree
        if not root:
            return 0
        
        # Recursive case: 1 + max depth of subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
    
    def maxDepthIterativeBFS(self, root: Optional[TreeNode]) -> int:
        """
        Find maximum depth using iterative BFS (level order traversal).
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Maximum depth of the tree
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width of tree
        """
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            level_size = len(queue)
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
    
    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        """
        Find maximum depth using iterative DFS with stack.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Maximum depth of the tree
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return 0
        
        stack = [(root, 1)]  # (node, current_depth)
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        
        return max_depth


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


def test_maximum_depth_binary_tree():
    """Test cases for Maximum Depth of Binary Tree."""
    solution = Solution()
    
    # Test case 1: Example from problem
    root = list_to_tree([3, 9, 20, None, None, 15, 7])
    assert solution.maxDepth(root) == 3
    
    # Test case 2: Single node
    root = list_to_tree([1])
    assert solution.maxDepth(root) == 1
    
    # Test case 3: Empty tree
    assert solution.maxDepth(None) == 0
    
    # Test case 4: Left-skewed tree
    root = list_to_tree([1, 2, None, 3, None, 4])
    assert solution.maxDepth(root) == 4
    
    # Test case 5: Right-skewed tree
    root = list_to_tree([1, None, 2, None, 3])
    assert solution.maxDepth(root) == 3
    
    # Test case 6: Balanced tree
    root = list_to_tree([1, 2, 3, 4, 5, 6, 7])
    assert solution.maxDepth(root) == 3
    
    # Test iterative BFS
    root = list_to_tree([3, 9, 20, None, None, 15, 7])
    assert solution.maxDepthIterativeBFS(root) == 3
    
    # Test iterative DFS
    root = list_to_tree([3, 9, 20, None, None, 15, 7])
    assert solution.maxDepthIterativeDFS(root) == 3
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_maximum_depth_binary_tree()
