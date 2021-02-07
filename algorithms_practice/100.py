"""100 Same Tree Easy
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.same = True
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_v = getattr(p, "val", None)
        q_v = getattr(q, "val", None)
        if p_v != q_v:
            self.same = False
        if not any([p_v is None, q_v is None]):
            self.isSameTree(p.left, q.left)
            self.isSameTree(p.right, q.right)
        return self.same
