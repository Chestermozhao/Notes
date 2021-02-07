"""83. Remove Duplicates from Sorted List Easy
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        seen = set()
        current_node = head
        if head is not None:
            seen.add(current_node.val)
        else:
            return head

        while current_node.next:
            if current_node.next.val in seen:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                seen.add(current_node.val)
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        seen = set()
        current_node = ListNode()
        answer = current_node
        while head.next:
            if head.val not in seen:
                current_node.next = ListNode(val=head.val)
                current_node = current_node.next
                seen.add(head.val)
            head = head.next
        
        if head.val not in seen:
            current_node.next = ListNode(val=head.val)
        return answer.next
