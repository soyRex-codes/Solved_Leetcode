"""
LeetCode 21: Merge Two Sorted Lists

Problem:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists. Return the head of the merged linked list.

Approach:
Use a dummy node to simplify edge cases.
Compare nodes from both lists and attach the smaller one.
Move pointer forward in the list from which we took the node.
After one list is exhausted, attach the remainder of the other list.

Time Complexity: O(n + m) where n and m are lengths of the two lists
Space Complexity: O(1) - only using constant extra space

Example:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists.
        
        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list
            
        Returns:
            Head of merged sorted linked list
        """
        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (at most one list has remaining nodes)
        current.next = list1 if list1 else list2
        
        return dummy.next
    
    def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists recursively.
        
        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list
            
        Returns:
            Head of merged sorted linked list
        
        Time Complexity: O(n + m)
        Space Complexity: O(n + m) due to recursion stack
        """
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive case: choose smaller node and merge rest
        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2


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


def test_merge_two_sorted_lists():
    """Test cases for Merge Two Sorted Lists."""
    solution = Solution()
    
    # Test case 1: Both lists have multiple nodes
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]
    
    # Test case 2: One empty list
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [0]
    
    # Test case 3: Both empty lists
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == []
    
    # Test case 4: Lists of different lengths
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4])
    merged = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 7]
    
    # Test recursive version
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoListsRecursive(list1, list2)
    assert linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_merge_two_sorted_lists()
