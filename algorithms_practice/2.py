"""Leetcode 2 Medium
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trans_to_ll(self, num):
        ll = None
        _num = str(num)
        for i, item in enumerate(_num):
            if i == 0:
                ll = ListNode(val=item)
            else:
                ll = ListNode(val=item, next=ll)
        return ll
    
    def get_num(self, ll):
        num = ""
        val = ll.val
        while val is not None:
            num = str(val) + num
            ll = ll.next
            if ll is None:
                break
            val = ll.val
        return int(num)
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        total_num = num1 + num2
        transed_ll = self.trans_to_ll(total_num)
        return transed_ll
