"""82. Remove Duplicates from Sorted List II Medium
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = ListNode()
        answer = node
        existed = set()
        while head.next:
            if head.val != head.next.val and head.val not in existed:
                node.next = ListNode(val=head.val)
                node = node.next
            else:
                existed.add(head.val)
            head = head.next
        if head.val not in existed:
            node.next = ListNode(val=head.val)
        return answer.next
