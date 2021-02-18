"""Palindrome Linked List
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.pre_order_l = []
        self.post_order_l = []
        
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        self.pre_order_l.append(head.val)
        self.isPalindrome(head.next)
        self.post_order_l.append(head.val)
        if self.pre_order_l == self.post_order_l:
            return True
