from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is not None:
            res.append(root.val)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is not None:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is not None:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.val)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        ans = []
        cur = []
        _next = []
        cur.append(root)
        while cur:
            _ans = []
            for item in cur:
                _ans.append(item.val)
                if item.left:
                    _next.append(item.left)
                if item.right:
                    _next.append(item.right)
            ans.append(_ans)
            cur = _next
            _next = []
        return ans

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return all(
            [
                t1.val == t2.val,
                self.is_mirror(t1.left, t2.right),
                self.is_mirror(t1.right, t2.left)
            ]
        )

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        is_has_sum_left = self.hasPathSum(root.left, targetSum-root.val)
        is_has_sum_right = self.hasPathSum(root.right, targetSum-root.val)
        return any([is_has_sum_left, is_has_sum_right])

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        root = preorder[0]
        root_index = inorder.index(root)
        left_tree = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        right_tree = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return TreeNode(root, left_tree, right_tree)

    # 116
    def connect(self, root: 'Node') -> 'Node':
        if root is None or root.left is None:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    # 117
    def connect(self, root: 'Node') -> 'Node':
        if root is None or all([root.left is None, root.right is None]):
            return root
        cur = [root]
        _next = []
        while cur:
            for i in range(len(cur)):
                if cur[i].left:
                    _next.append(cur[i].left)
                if cur[i].right:
                    _next.append(cur[i].right)
                if i+1 >= len(cur):
                    break
                cur[i].next = cur[i+1]
            cur = _next
            _next = []
        return root


root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))


solution = Solution()
solution.preorderTraversal(root)
