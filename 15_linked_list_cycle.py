"""
LeetCode 141: Linked List Cycle

Problem:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be 
reached again by continuously following the next pointer.

Approach:
Use Floyd's Cycle Detection Algorithm (Tortoise and Hare):
- Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
- If there's a cycle, fast will eventually catch up to slow
- If there's no cycle, fast will reach the end (None)

Time Complexity: O(n) - in worst case, we visit each node once
Space Complexity: O(1) - only using two pointers

Example:
    Input: head = [3,2,0,-4], pos = 1 (cycle connects to node at index 1)
    Output: true
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if linked list has a cycle using Floyd's algorithm.
        
        Args:
            head: Head of the linked list
            
        Returns:
            True if there is a cycle, False otherwise
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        # Move slow by 1 and fast by 2
        # If they meet, there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def hasCycleWithSet(self, head: Optional[ListNode]) -> bool:
        """
        Alternative solution using hash set.
        
        Args:
            head: Head of the linked list
            
        Returns:
            True if there is a cycle, False otherwise
        
        Time Complexity: O(n)
        Space Complexity: O(n) - hash set to store visited nodes
        """
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        
        return False
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the node where the cycle begins (bonus method).
        
        Args:
            head: Head of the linked list
            
        Returns:
            Node where cycle begins, or None if no cycle
        
        Algorithm:
        1. Use Floyd's algorithm to detect cycle
        2. If cycle exists, reset one pointer to head
        3. Move both pointers one step at a time
        4. They will meet at the cycle start
        """
        if not head or not head.next:
            return None
        
        # Phase 1: Detect cycle
        slow = head
        fast = head
        has_cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                has_cycle = True
                break
        
        if not has_cycle:
            return None
        
        # Phase 2: Find cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow


def create_linked_list_with_cycle(values, pos):
    """
    Helper function to create linked list with a cycle.
    pos indicates the index where the cycle connects (-1 for no cycle).
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    cycle_node = None
    
    if pos == 0:
        cycle_node = head
    
    for i, val in enumerate(values[1:], 1):
        curr.next = ListNode(val)
        curr = curr.next
        if i == pos:
            cycle_node = curr
    
    # Create cycle if pos is valid
    if pos != -1 and cycle_node:
        curr.next = cycle_node
    
    return head


def test_linked_list_cycle():
    """Test cases for Linked List Cycle."""
    solution = Solution()
    
    # Test case 1: Has cycle
    head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert solution.hasCycle(head) == True
    
    # Test case 2: No cycle
    head = create_linked_list_with_cycle([1, 2], -1)
    assert solution.hasCycle(head) == False
    
    # Test case 3: Single node with cycle to itself
    head = create_linked_list_with_cycle([1], 0)
    assert solution.hasCycle(head) == True
    
    # Test case 4: Empty list
    assert solution.hasCycle(None) == False
    
    # Test case 5: Single node without cycle
    head = create_linked_list_with_cycle([1], -1)
    assert solution.hasCycle(head) == False
    
    # Test with hash set approach
    head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert solution.hasCycleWithSet(head) == True
    
    # Test detectCycle
    head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    cycle_start = solution.detectCycle(head)
    assert cycle_start is not None and cycle_start.val == 2
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_linked_list_cycle()
