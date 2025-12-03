"""
LeetCode 206: Reverse Linked List

Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach:
Use iterative approach with three pointers:
- prev: previous node (starts as None)
- curr: current node (starts at head)
- next: next node (temporary storage)

For each iteration:
1. Store next node
2. Reverse current node's pointer to previous
3. Move prev and curr forward

Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - only using constant extra space

Example:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list iteratively.
        
        Args:
            head: Head of the linked list
            
        Returns:
            Head of the reversed linked list
        """
        prev = None
        curr = head
        
        while curr:
            # Store next node
            next_node = curr.next
            
            # Reverse current node's pointer
            curr.next = prev
            
            # Move pointers forward
            prev = curr
            curr = next_node
        
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list recursively.
        
        Args:
            head: Head of the linked list
            
        Returns:
            Head of the reversed linked list
        
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        
        # Reverse the current node's connection
        head.next.next = head
        head.next = None
        
        return new_head


def create_linked_list(values):
    """Helper function to create linked list from list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to list for testing."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def test_reverse_linked_list():
    """Test cases for Reverse Linked List."""
    solution = Solution()
    
    # Test case 1: Multiple nodes
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = solution.reverseList(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]
    
    # Test case 2: Two nodes
    head = create_linked_list([1, 2])
    reversed_head = solution.reverseList(head)
    assert linked_list_to_list(reversed_head) == [2, 1]
    
    # Test case 3: Single node
    head = create_linked_list([1])
    reversed_head = solution.reverseList(head)
    assert linked_list_to_list(reversed_head) == [1]
    
    # Test case 4: Empty list
    reversed_head = solution.reverseList(None)
    assert reversed_head is None
    
    # Test recursive version
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = solution.reverseListRecursive(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_linked_list()
