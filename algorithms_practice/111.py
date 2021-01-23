"""Leetcode 111 Easy
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
-----
Input: root = [3,9,20,null,null,15,7]
Output: 2
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        depth = 1
        while q:
            next_q = []
            for i, item in enumerate(q):
                if item.left is None and item.right is None:
                    return depth
                if item.left:
                    next_q.append(item.left)
                if item.right:
                    next_q.append(item.right)
            q = next_level
            depth += 1
        return depth
